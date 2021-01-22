import os,sys
# from setting import *
from testfile import getpathInfo

log_path = os.path.join(getpathInfo.get_root_path(), "result", "logs")
report_html = os.path.join(getpathInfo.get_root_path(), "result", "html")
read_xlrd = os.path.join(getpathInfo.get_root_path(), "testfile", "case", "userCase.xlsx")

class Common():
    #封装日志方法
    def get_logs(self,path = log_path):
        import logging, time
        logs = logging.getLogger()
        logs.setLevel(logging.DEBUG)
        path = path +'/' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.log'
        write_file = logging.FileHandler(path, 'a+', encoding='utf-8')
        write_file.setLevel(logging.DEBUG)
        set_logs = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
        write_file.setFormatter(set_logs)
        pycharm_text = logging.StreamHandler()
        pycharm_text.setFormatter(set_logs)
        logs.addHandler(write_file)
        logs.addHandler(pycharm_text)
        return logs

    # 读取Excel表方法，方便后续读取接口用例数据
    def ReadExcelTypeDict(self, file_name, path=read_xlrd):
        path = path +'/' + file_name
        import xlrd
        work_book = xlrd.open_workbook(path)  # 打开Excel表
        sheets = work_book.sheet_names()  # 获取所有的sheets页
        DatasList = []
        for sheet in sheets:
            sheets = work_book.sheet_by_name(sheet)
            nrows = sheets.nrows
            for i in range(0,nrows):
                values = sheets.row_values(i)
                DatasList.append(values)
        title_list = DatasList[0]
        content_list = DatasList[1:]
        new_list = []
        for content in content_list:
            dic = {}
            for i in range(len(content)):
                dic[title_list[i]] = content[i]
            new_list.append(dic)
        return new_list   #最终返回为字典形式 有键和值

    # 封装一个HTML报告方法
    def GetHtmlResult(self, suite, title, path = report_html):
        import common.HTMLTestReportCN as HTMLTestReportCN
        import time
        path = path + '/' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.html'
        with open(path, 'wb+') as f:
            run = HTMLTestReportCN.HTMLTestRunner(stream=f, description='用户相关接口测试报告', tester='stt', title = title)
            run.run(suite)