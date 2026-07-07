"""测试用例：通用口令"""
import paramiko
import pymysql
import redis

# 多个子系统复用同一默认口令
DEFAULT_PASSWORD = "P@ssw0rd123"


def connect_mysql():
    return pymysql.connect(
        host="192.168.1.10",
        user="root",
        password=DEFAULT_PASSWORD,
        database="orders",
    )


def connect_redis():
    return redis.Redis(host="192.168.1.11", password=DEFAULT_PASSWORD)


def deploy_via_ssh(host: str):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username="deploy", password=DEFAULT_PASSWORD)
    return client
