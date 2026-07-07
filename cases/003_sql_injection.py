"""测试用例：SQL注入"""
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # 直接拼接用户输入到 SQL
    query = f"SELECT id, name, email FROM users WHERE id = {user_id}"
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return {"user": row}
