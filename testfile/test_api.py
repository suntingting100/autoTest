# 自己写的提供本地测试的接口服务

import flask
import json
from flask import request

"""
flask:web框架，通过flask提供的装饰器@server.route（）将普通函数转换为服务
"""

# 创建一个服务
server = flask.Flask(__name__)
# @server.route（）可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route("/login", methods=["get", "post"])
def login():
    username = request.values.get("name")
    pwd = request.values.get("pwd")
    if username and pwd:
        if username == "xiaoming" and pwd == "111":
            resu = {"code": 200, "message": "登录成功"}
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {"code": -1, "message": "账号密码错误"}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu =  {"code": 100001, "message": "参数不能为空"}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == "__main__":
    server.run(debug=True, port=8888, host="127.0.0.1")
