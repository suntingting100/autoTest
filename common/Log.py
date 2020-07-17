# 调用该类的方法，用来打印生成日志

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from testfile import getpathInfo

path = getpathInfo.get_Path()
log_path = os.path.join(path, "result") # 存放log文件的


class Logger(object):
    def __init__(self, logger_name="log..."):
        self.logger = logging.getLogger(logger_name)git
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = "Logs"  # 日志文件的名称
        self.backup_count = 5 # 最多存放日志的数量
        # 日志输出级别
        self.console_output_level = "WARNING"
        self.file_out_level = "DEBUG"
        # 日志输出格式
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    def get_logger(self)
        """
        在logger中添加日志句柄并返回，如果logger中已有句柄，则直接返回
        :return: 
        """
        if not self.logger.handlers: # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.handlers(console_handler)

            # 每天重新创建一个日志文件，最多保留back_up份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when="D,",
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding="utf-8")
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_out_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()



