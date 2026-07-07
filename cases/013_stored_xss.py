"""测试用例：存储型跨站脚本"""
import sqlite3
from flask import Flask, request
from markupsafe import Markup

app = Flask(__name__)


@app.route("/comment", methods=["POST"])
def add_comment():
    content = request.form.get("content", "")
    conn = sqlite3.connect("app.db")
    conn.execute("INSERT INTO comments(content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    return {"ok": True}


@app.route("/comments")
def list_comments():
    conn = sqlite3.connect("app.db")
    rows = conn.execute("SELECT content FROM comments ORDER BY id DESC LIMIT 20").fetchall()
    conn.close()
    # 原样输出用户 HTML/JS，浏览器会直接执行
    html = "<br>".join(Markup(row[0]) for row in rows)
    return f"<html><body>{html}</body></html>"
