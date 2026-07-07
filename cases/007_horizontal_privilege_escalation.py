"""测试用例：水平越权"""
import sqlite3
from flask import Flask, request, g

app = Flask(__name__)


def current_user_id():
    return int(request.headers.get("X-User-Id", "0"))


@app.route("/profile/<int:user_id>")
def get_profile(user_id: int):
    # 未校验 user_id 是否属于当前登录用户
    conn = sqlite3.connect("app.db")
    row = conn.execute(
        "SELECT id, phone, id_card, balance FROM users WHERE id = ?",
        (user_id,),
    ).fetchone()
    conn.close()
    return {"profile": row, "viewer": current_user_id()}
