"""测试用例：任意文件上传"""
import os
from flask import Flask, request

app = Flask(__name__)
UPLOAD_DIR = "/var/www/uploads"


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    # 未校验扩展名、MIME、内容，直接保存用户提供的文件名
    save_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(save_path)
    return {"ok": True, "path": save_path}
