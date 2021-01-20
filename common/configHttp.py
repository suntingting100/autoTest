# 这个文件来通过get， post， put， delete等方法来进行http请求，把那个拿到请求响应

import requests
import json
import warnings
import urllib3

warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# class RunMain():
#
#     def send_get(self, url, data):
#         result = requests.get(url=url, params=data).json()
#         res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#         return res
#
#     def send_post(self, url, data):
#         result = requests.post(url=url, json=data, verify=False).json()
#         res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#         return res
#
#     def send_put(self, url, data):
#         result = requests.put(url=url, json=data).json()
#         res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#         return res
#
#     def send_delete(self, url, data):
#         result = requests.delete(url=url, json=data).json()
#         res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#         return res
#
#     def run_main(self, method, url=None, data=None):
#         result = None
#         if method == "post":
#             result = self.send_post(url, data)
#         elif method == "get":
#             result = self.send_get(url, data)
#         elif method == "put":
#             result = self.send_put(url, data)
#         elif method == "delete":
#             result = self.send_delete(url, data)
#         else:
#             print("method值错误")
#         return result
#
#
# if __name__ == "__main__":
#     result1 = RunMain().run_main("post", "https://tapi.quanziapp.com/api/v2/login", {"device_id":"C55F24F2-A927-4125-8D3A-D0379B90F4D3","device_type":"web","device_name":"Chrome","device_system":"Win32","app_version":"pc web v3.3.2","mobile":{"country_code":"86","phone_number":"15210801234","password":"123456"}})
#     print(result1)

class Base(method_):


    def requests_type(self, method, url, params=None, data=None, headers=None, files=None):
        if method == 'post' or method == 'POST':
            return self.method_post(url=url, params=params, data=data, headers=headers, files=files)
        elif method == 'get' or method == 'GET':
            return self.method_get(url=url, params=params, data=data, headers=headers, files=files)
        elif method == 'put' or method == 'PUT':
            return requests.put(url=url, params=params, data=data, headers=headers, files=files)
        elif method == 'delete' or method == 'DELETE':
            return requests.delete(url=url, params=params, data=data, headers=headers, files=files)


s = Base()
a = s.requests_type(method="post", url="https://tapi.quanziapp.com/api/v2/login",
                    data={"device_id": "C55F24F2-A927-4125-8D3A-D0379B90F4D3", "device_type": "web",
                          "device_name": "Chrome", "device_system": "Win32", "app_version": "pc web v3.3.2",
                          "mobile": {"country_code": "86", "phone_number": "15210801234",
                                     "password": "123456"}})
print(a)
