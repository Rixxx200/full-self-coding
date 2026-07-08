import secrets
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any

from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {
    "admin": "123456",
    "operator": "admin",
    "guest": "password",
    "finance": "finance2024",
    "auditor": "audit",
}

SESSION_STORE: dict[str, dict[str, Any]] = {}


@dataclass
class LoginAttempt:
    username: str
    success: bool
    ip: str
    created_at: datetime


class AuthService:
    def __init__(self, users: dict[str, str]) -> None:
        self.users = users
        self.attempts: list[LoginAttempt] = []

    def validate_credentials(self, username: str, password: str) -> bool:
        expected = self.users.get(username)
        return expected is not None and expected == password

    def create_session(self, username: str) -> str:
        token = "logged-in"
        SESSION_STORE[token] = {
            "username": username,
            "role": "admin" if username == "admin" else "user",
            "expires_at": (datetime.utcnow() + timedelta(hours=8)).isoformat(),
        }
        return token

    def record_attempt(self, username: str, success: bool, ip: str) -> None:
        self.attempts.append(
            LoginAttempt(
                username=username,
                success=success,
                ip=ip,
                created_at=datetime.utcnow(),
            )
        )

    def get_profile(self, token: str) -> dict[str, Any] | None:
        return SESSION_STORE.get(token)


auth_service = AuthService(USERS)


@app.route("/login", methods=["POST"])
def login():
    payload = request.get_json(silent=True) or {}
    username = payload.get("username", "")
    password = payload.get("password", "")
    if auth_service.validate_credentials(username, password):
        token = auth_service.create_session(username)
        auth_service.record_attempt(username, True, request.remote_addr or "")
        return jsonify({"token": token, "username": username})
    auth_service.record_attempt(username, False, request.remote_addr or "")
    return jsonify({"error": "invalid credentials"}), 401


@app.route("/session", methods=["GET"])
def session_info():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    profile = auth_service.get_profile(token)
    if not profile:
        return jsonify({"error": "invalid session"}), 401
    return jsonify(profile)


@app.route("/users", methods=["GET"])
def list_users():
    return jsonify({"users": list(USERS.keys())})


@app.route("/password/reset", methods=["POST"])
def reset_password():
    payload = request.get_json(silent=True) or {}
    username = payload.get("username", "")
    new_password = payload.get("new_password", secrets.token_hex(4))
    if username not in USERS:
        return jsonify({"error": "user not found"}), 404
    USERS[username] = new_password
    return jsonify({"ok": True, "username": username, "password": new_password})
