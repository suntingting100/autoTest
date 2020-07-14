# 调用该类的方法，用来打印生成日志

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from testfile import getpathInfo

path = getpathInfo.get_Path()
log_path = os.path.join(path, "result") # 存放log文件的


class Logger(object):
    def __init__(self, logger_name="log..."):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = "Logs"  # 日志文件的名称

        ###111
        
        
       # 222远程分支上改的
        
