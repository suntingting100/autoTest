"""
输出的值转成字符串
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式
"""

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end="")
    print(repr(x*x*x).rjust(4))

# str.format
for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))

print("{0} {1}".format("Google","Runnob"))
print("{1} {0}".format("Google","Runnob"))

print("{name}网址: {site}".format(name="菜鸟教程", site="www.runnob.com"))

table = {"Google": 1, "Runnob": 2, "Taobao": 3}
for name, number in table.items():
    print("{0:10} ===> {1:10d}".format(name, number))


# 读取键盘输入 input()函数
str = input("请输入： ")
print("你输入的内容是：", str)

# 读和写文件 open() 将会返回一个 file 对象，基本语法格式如下:open(filename, mode)

