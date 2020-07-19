import os
import common.HTMLTestRunner as HTMLTestRunner
from testfile import getpathInfo
import unittest
from testfile import readConfig
from common.configEmail import SendEmail
import common.Log
# from app import resultPath
# from apscheduler.schedulers.blocking import BlockingScheduler


send_email = SendEmail(
    username="617587058@qq.com",
    passwd="vmmmipmktibibcgj",
    recv=["617587058@qq.com"],
    title="测试报告",
    content="测试发送邮件",
    file=r"C:\Users\mi\PycharmProjects\project\测试截图\smtp2.jpg",
    ssl=True
)
path = getpathInfo.get_root_path()
report_path = os.path.join(path, "result")
on_off = readConfig.ReadConfig().get_email("on_off")
log = common.Log.logger

resultPath = ""


class AllTest:
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path, "report.html")

        self.caseListFile = os.path.join(path, "caseList.txt")
        self.caseFile = os.path.join(path, "case")
        self.caseList = []
        log.info(resultPath)  # 将resultpath的值输入到日志，方便定位查看问题
        log.info("caseListFile" + self.caseListFile)
        log.info(self.caseList)

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile, encoding="utf-8")
        for value in fb.readlines():
            data = str(value)
            if data != "" and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suit(self):
        """

        :return:
        """
        self.set_case_list()
        test_suit = unittest.TestSuite()
        suit_moudle = []
        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + ".py", top_level_dir=None)
            suit_moudle.append(discover)
            print("suit_moudle:" + str(suit_moudle))
        if len(suit_moudle) > 0:
            for suit in suit_moudle:
                for test_name in suit:
                    test_suit.addTests(test_name)
        else:
            print("else:")
            return None
        return test_suit

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suit()
            print("try")
            print(str(suit))
            if suit is not None:
                print("if-suit")
                fp = open(resultPath, "wb")
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Test Report", description="Test Description")
                runner.run(suit)
                fp.close()
            else:
                print("Have no case to test")
        except Exception as ex:
            print(str(ex))
        finally:
            print("********TEST END*********")

        # 判断邮件发送的开关
        if on_off == "on":
            send_email.send_email()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常发送测试报告")


if __name__ == "__main__":
    AllTest().run()
    # AllTest().set_case_list()
    # AllTest().set_case_suit()
