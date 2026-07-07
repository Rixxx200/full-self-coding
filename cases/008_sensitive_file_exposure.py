"""测试用例：敏感文件泄露"""
import os
from flask import Flask, send_file

app = Flask(__name__)
PUBLIC_ROOT = "/var/www/html"


@app.route("/download/<path:filename>")
def download_backup(filename: str):
    # 备份、源码等敏感文件与静态资源放在同一可访问目录
    file_path = os.path.join(PUBLIC_ROOT, "backups", filename)
    return send_file(file_path, as_attachment=True)
