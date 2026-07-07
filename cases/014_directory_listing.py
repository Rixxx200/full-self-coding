"""测试用例：列目录"""
import os
from flask import Flask

app = Flask(__name__)
STATIC_ROOT = "/var/www/static"


@app.route("/files/")
@app.route("/files/<path:subpath>")
def browse_files(subpath: str = ""):
    target = os.path.join(STATIC_ROOT, subpath)
    entries = os.listdir(target)
    # 直接列出目录内容，暴露隐藏文件和备份
    listing = "\n".join(f"<li><a href='{entry}'>{entry}</a></li>" for entry in entries)
    return f"<ul>{listing}</ul>"
