# 读取userCase.xlsx中的用例，使用pytest来进行断言校验

import json
import unittest
from common.configHttp import RunMain
import paramunittest
from testfile.geturlParams import geturlParams
import urllib.parse
# import pythoncom
from testfile.readExcel import readExcel
# pythoncom.CoInitialize

url = geturlParams().get_url()
login_xls = readExcel().get_xls("userCase.xlsx", "login")


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = query
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name + "测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        host = "https://tapi.quanziapp.com"
        url1 = host + self.path
        info = RunMain().run_main(self.method, url1, self.query)
        print(info)
        ss = json.loads(info)
        print(ss)
        if self.case_name == "login":
            self.assertEquals(ss["id"], "j7X7rk")
        if self.case_name == "login_error":
            self.assertEquals(ss["code"], "wrong_password")
