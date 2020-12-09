"""
github第二种登录方式
info:
author:suntingting
github:https://github.com/CriseLYJ/
update_time:2020--8-31
"""

import re
import requests
from lxml import etree

# gitclass login(object):
class Githublogin(object):

    def __init__(self, email, password):

        # 初始化信息
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/',
            'Host': 'github.com'
        }
        self.sessions = requests.sessions()
        self.loginurl = 'https://github.com/login'
        self.posturl = 'https://github.com/session'
        self.sessions = requests.sessions()

        self.email = email
        self.password = password

        # 模拟登录
        def login_GitHub(self):

            # 登录入口
            post_data = {
                'commit': 'Sign in',
                'utf8': '✓',
                'authenticity_token': self.get_token(),
                'login': self.email,
                'password': self.password
            }

            resp = self.session.post(
                self.post_url, data=post_data, headers=self.headers
            )

            print("statuscode:", resp.status_code)

            if resp.status_code != 200:
                print("login fail")

            match = re.search(r'"user-login" content="(.*?)"', resp.text)

            user_name = match.group(1)
            print("Username:", user_name)

            response = self.session.post(self.post_url, data=post_data, headers=self.headers)

            print(response.status_code)
            print(post_data)

            if response.status_code == 200:
                print("登录成功")
            else:
                print("登录失败")





