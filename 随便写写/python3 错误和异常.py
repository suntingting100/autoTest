
"""
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
OSError:
ValueError
IOError
ZeroDivisionError
AssertionError
NameError
"""

"""
异常处理：异常捕捉可以使用 try/except 语句。
"""
# while True:
#     try:
#         x = int(input("请输入一个数字："))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入")


"""
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
except (RuntimeError, TypeError, NameError):
    pass
"""


# import sys, traceback
#
# try:
#     f = open("/Users/taten/Desktop/linux文件", "r")
#     s = f.readline()
#     i = int(s.strip("1")) # 去掉1; 什么都不填是去首尾空格
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     # sys.exc_info()返回的值是一个元组，其中第一个元素，[exc_type是异常的对象类型，exc_value是异常的值，exc_tb是一个traceback对象]，对象中包含出错的行数、位置等数据。
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


"""
try/except...else
"""

import sys

# sys.argv 是获取当前文件的绝对路径

# for arg in sys.argv:
#     try:
#         f = open(arg, "r")
#     except IOError:
#         print("cannot open", arg)
#     else:
#         print(arg, "has", len(f.readlines()), "lines")
#         f.close()


# def this_fails():
#     x = 1/0
#
#
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print("Handing run-time occurred, value:", err)


"""
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
"""

# try:
#     runoob()
# except NameError as error:
#     print(error)
# else:
#     try:
#         with open("/Users/taten/Desktop/Linux文件") as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print("这句话，无论异常是否会发生都会执行")

"""
抛出异常
Python 使用 raise 语句抛出一个指定的异常。
raise语法格式如下：raise [Exception [, args [, traceback]]]
"""
# x = 10
# if x > 5:
#     raise Exception("x不能大于5。x的值为：{}".format(x))
#
# try:
#     raise NameError("HiThere")
# except NameError:
#     print("An exception flew by")
#     raise

"""
用户自定义异常
"""


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print("My exception occurred, value:", e.value)






