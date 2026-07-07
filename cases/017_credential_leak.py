"""测试用例：登录账户和密码泄露"""
import logging
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger("auth")


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    logger.info("user login attempt username=%s password=%s ip=%s", username, password, request.remote_addr)
    if username == "admin" and password == "admin123":
        return {
            "ok": True,
            "debug": {"username": username, "password": password},
        }
    return {"ok": False, "hint": f"password for {username} is incorrect"}, 401
