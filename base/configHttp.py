import requests
import json
import warnings
import urllib3

warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Base():

    def send_post(self, url, params=None, data=None, headers=None, files=None):
        result = requests.post(url=url, params=params, json=data, headers=headers, files=files, verify=False).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, params=None, data=None, headers=None, files=None):
        result = requests.get(url=url, params=params, data=data, headers=headers, files=files).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_put(self, url, params=None, data=None, headers=None, files=None):
        result = requests.put(url=url, params=params, data=data, headers=headers, files=files).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_delete(self, url, params=None, data=None, headers=None, files=None):
        result =  requests.delete(url=url, params=params, data=data, headers=headers, files=files).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def requests_type(self, method, url, params=None, data=None, headers=None, files=None):
        result = None
        if method == 'post' or method == 'POST':
            result =  self.send_post(url=url, params=params, data=data, headers=headers, files=files)
        elif method == 'get' or method == 'GET':
            result = self.send_get(url=url, params=params, data=data, headers=headers, files=files)
        elif method == 'put' or method == 'PUT':
            result = self.send_put(url=url, params=params, data=data, headers=headers, files=files)
        elif method == 'delete' or method == 'DELETE':
            result = self.send_delete(url=url, params=params, data=data, headers=headers, files=files)
        return result


if __name__ == "__main__":
    result = Base().requests_type(method="post", url="https://tapi.quanziapp.com/api/v2/login",
                                data={"device_id": "5CF088BF-7B03-458E-814B-CB7D0940D5D0", "device_type": "web",
                                 "device_name": "Chrome", "device_system": "Win32", "app_version": "pc web v3.3.2",
                                 "mobile": {"country_code": "86", "phone_number": "15210801234", "password": "123456"}})
    print(result)