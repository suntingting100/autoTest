import logging
import time
import os,sys
# from setting import *
from testfile import getpathInfo


class Log:

    # 日志路径, 这里我写的自己配置的路径
    log = ('report_' + '%s' % time.strftime("%Y-%m-%d", time.localtime()) + '.log').replace('\\', '/')
    path = getpathInfo.get_root_path()
    log_path = os.path.join(path, "result", log)

    def __init__(self):
        # 文件的命名
        self.logname = self.log_path
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='UTF-8')  # 追加模式
        fh.setLevel(logging.DEBUG)
        # fh.setLevel(logging.WARNING)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # ch.setLevel(logging.WARNING)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
   log = Log()
   log.
   log.info("这是一个info")
   log.error("这是一个error")
   log.warning("这是一个warning")