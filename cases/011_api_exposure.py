"""测试用例：API接口泄露"""
from flask import Flask, jsonify

app = Flask(__name__)
CUSTOMERS = [
    {"id": 1, "name": "张三", "phone": "13800000001", "id_card": "110101199001011234"},
    {"id": 2, "name": "李四", "phone": "13800000002", "id_card": "110101199002021234"},
]


@app.route("/api/v1/customers/export")
def export_customers():
    # 无 Token、无签名、无 IP 白名单
    return jsonify({"total": len(CUSTOMERS), "items": CUSTOMERS})


@app.route("/api/internal/debug/reset", methods=["POST"])
def reset_cache():
    return {"reset": True}
