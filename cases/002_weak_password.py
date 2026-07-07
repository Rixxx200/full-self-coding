"""测试用例：弱口令"""
from flask import Flask, request

app = Flask(__name__)

# 硬编码弱口令，无复杂度策略
USERS = {
    "admin": "123456",
    "operator": "admin",
    "guest": "password",
}


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if USERS.get(username) == password:
        return {"token": "logged-in"}
    return {"error": "invalid credentials"}, 401
