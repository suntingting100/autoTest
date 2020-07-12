# 读取userCase.xlsx中的用例，使用pytest来进行断言校验

import json
import unittest
from common.configHttp import RunMain
import paramuinttest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
# pythoncom.CoInitialize

url = geturlParams().get_Url()
login_xls = readExcel.get_xls("userCase.xlsx", "login")


@paramuinttest.parametrized(*login_xls)
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
        self.query = str(query)
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
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        info = RunMain().run_main(self.method, url, data1)
        ss = json.loads(info)
        if self.case_name == "login":
            self.assertEquals(ss["code"], 200)
        if self.case_name == "login_error":
            self.assertEquals(ss["code"], -1)
        if self.case_name == "login_url":
            self.assertEquals(ss["code"], 10001)