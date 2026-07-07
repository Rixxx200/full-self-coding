"""测试用例：支付漏洞"""
from flask import Flask, request

app = Flask(__name__)
ORDERS = {}


@app.route("/pay", methods=["POST"])
def pay_order():
    data = request.json
    order_id = data["order_id"]
    # 金额、状态完全信任客户端，未与服务端订单核对
    amount = data.get("amount", 0)
    status = data.get("status", "paid")
    ORDERS[order_id] = {"amount": amount, "status": status}
    return {"paid": True, "amount": amount}
