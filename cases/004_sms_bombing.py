"""测试用例：短信轰炸"""
import requests
from flask import Flask, request

app = Flask(__name__)
SMS_GATEWAY = "https://sms.example.com/send"


@app.route("/send_sms", methods=["POST"])
def send_sms():
    phone = request.json.get("phone")
    message = request.json.get("message", "验证码：1234")
    # 无频率限制、无验证码、无单日上限
    requests.post(SMS_GATEWAY, json={"phone": phone, "text": message}, timeout=5)
    return {"sent": True}
