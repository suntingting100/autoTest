import requests
import os
import gevent
from gevent import monkey
from locust import HttpUser, TaskSet, task

base_url = "http://dev-game.duodian.cn"


class UserBehavior(TaskSet):
    @task
    def enter(self):
        headers = headers = {'content-type': 'application/json;charset=utf-8'}
        url_enter = base_url + "/api/team/third/enter"
        TeamThirdEnterParam = {
            "appId": 1001,
            "thirdUserId": "102402",
            "nickname": "102402",
            "avatar": "avatar",
            "sex": "1",
            "phone": "",
            "location": ""
        }
        req_enter = self.client.post(url=url_enter, json=TeamThirdEnterParam, headers=headers)
        if req_enter.status_code == 200:
            print("success")
        else:
            print("fails")


class EnterUser(HttpUser):
    task_set = UserBehavior
    min_wait = 300
    max_wait = 1000


# if __name__ == "__main__":
#     os.system("locust -f /Users/duodiankeji/Documents/Python/untitled/loacut/test.py  --host=192.168.1.117")