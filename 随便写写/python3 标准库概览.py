"""
操作系统接口
"""
# import os
# os.getcwd()   # 获取当前文件目录
# os.system("mkdir today")    # 创建文件夹


"""
文件通配符
"""
# import glob
# print(glob.glob("*.py"))


"""
命令行参数
"""
# import sys
# print(sys.argv)


"""
错误输出重定向和程序终止
"""
# import sys
# sys.stderr.write("warning,log file not find starting a new one \n")


"""
字符串正则匹配
"""
# import re
# re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
#
# "tea for too".replace("too", "two")

"""
数学
"""
# import math
# math.cos(math.pi, 4)
#
# import random
# random.choice("apple", "banana", "pear")
# random.sample(range(10, 100))


"""
访问互联网
"""
# from urllib.request import urlopen
# for line in urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
#     line = line.decode("utf-8")
#     if "EST" in line or "EDT" in line:
#         print(line)


# import smtplib
# server = smtplib.SMTP("localhost")
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# ... """To: jcaesar@example.org
# ... From: soothsayer@example.org
# ...
# ... Beware the Ides of March.
# ... """)
# server.quit()


"""
日期和时间：datetime模块为日期和时间处理同时提供了简单和复杂的方法。
"""
from datetime import date
now = date.today()
print(now)
