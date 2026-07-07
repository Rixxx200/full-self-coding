"""测试用例：其他安全问题（不安全反序列化）"""
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/session/load", methods=["POST"])
def load_session():
  raw = request.data
  # 直接反序列化不可信输入
  session_obj = pickle.loads(raw)
  return {"user": getattr(session_obj, "username", None)}
