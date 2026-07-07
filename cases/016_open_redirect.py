"""测试用例：URL重定向"""
from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/logout")
def logout():
    next_url = request.args.get("next", "/")
    # 未校验 next 是否为站内地址
    return redirect(next_url)


@app.route("/go")
def go():
    target = request.args.get("url")
    return redirect(target)
