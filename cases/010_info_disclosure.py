"""测试用例：其他信息泄露"""
import traceback
from flask import Flask, request

app = Flask(__name__)


@app.route("/search")
def search():
    keyword = request.args.get("q", "")
    try:
        if "'" in keyword:
            raise ValueError("bad keyword")
        return {"results": [keyword]}
    except Exception as exc:
        # 将完整堆栈和内部路径返回给前端
        return {
            "error": str(exc),
            "traceback": traceback.format_exc(),
            "sql": f"SELECT * FROM docs WHERE title LIKE '%{keyword}%'",
            "server": "prod-app-03.internal",
        }, 500
