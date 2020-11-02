"""
操作系统接口
"""
import os
os.getcwd()   # 获取当前文件目录
os.system("mkdir today")    # 创建文件夹


"""
文件通配符
"""
import glob
print(glob.glob("*.py"))


"""
命令行参数
"""
import sys
print(sys.argv)


"""
错误输出重定向和程序终止
"""
import sys
sys.stderr.write("warning,log file not find starting a new one \n")


"""
字符串正则匹配
"""
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

"tea for too".replace("too", "two")

"""
数学
"""
import math
math.cos(math.pi, 4)

import random
random.choice("apple", "banana", "pear")
random.sample(range(10, 100))