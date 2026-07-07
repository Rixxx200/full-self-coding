"""测试用例：配置信息泄露"""
from flask import Flask, send_file

app = Flask(__name__)

CONFIG_SNIPPET = """
MYSQL_HOST=10.0.0.8
MYSQL_USER=root
MYSQL_PASSWORD=SuperSecret_DB_Pass!
JWT_SECRET=hardcoded-jwt-secret-key
OSS_ACCESS_KEY=AKIAEXAMPLEKEY
OSS_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
"""


@app.route("/.env")
def expose_env():
    return CONFIG_SNIPPET, 200, {"Content-Type": "text/plain"}


@app.route("/config/download")
def download_config():
    return send_file("/etc/app/settings.yaml", as_attachment=True)
