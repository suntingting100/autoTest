
"""
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
"""

"""
异常处理：异常捕捉可以使用 try/except 语句。
"""
while True:
    try:
        x = int(input("请输入一个数字："))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入")


"""
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
except (RuntimeError, TypeError, NameError):
    pass
"""
""
import sys

try:
    f = open("/Users/taten/Desktop/linux文件", "r")
    s = f.readline()
    i = int(s.strip("1")) # 去掉1; 什么都不填是去首尾空格
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise












