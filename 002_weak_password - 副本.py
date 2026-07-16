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