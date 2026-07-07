"""测试用例：其他未授权访问"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/admin/users")
def list_all_users():
    # 管理接口无任何登录或角色校验
    users = [
        {"id": 1, "name": "alice", "role": "admin"},
        {"id": 2, "name": "bob", "role": "user"},
    ]
    return jsonify(users)


@app.route("/internal/metrics")
def internal_metrics():
    return {
        "db_host": "10.0.0.5",
        "active_sessions": 128,
        "pending_jobs": 42,
    }
