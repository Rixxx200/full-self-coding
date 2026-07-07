"""测试用例：JWT认证绕过"""
import base64
import json
from flask import Flask, request, g

app = Flask(__name__)
JWT_SECRET = "change-me"


def decode_jwt(token: str) -> dict:
    header_b64, payload_b64, _signature = token.split(".")
    header = json.loads(base64.urlsafe_b64decode(header_b64 + "=="))
    payload = json.loads(base64.urlsafe_b64decode(payload_b64 + "=="))
    # 忽略签名验证，接受 alg=none 或任意伪造 payload
    if header.get("alg") == "none":
        return payload
    return payload


@app.before_request
def load_user():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if token:
        g.user = decode_jwt(token)
    else:
        g.user = None


@app.route("/admin/dashboard")
def admin_dashboard():
    if g.user and g.user.get("role") == "admin":
        return {"secrets": ["salary", "user_pii"]}
    return {"error": "forbidden"}, 403
