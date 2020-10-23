# """
# 输出的值转成字符串
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式
# """
#
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end="")
#     print(repr(x*x*x).rjust(4))
#
# # str.format
# for x in range(1, 11):
#     print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))
#
# print("{0} {1}".format("Google","Runnob"))
# print("{1} {0}".format("Google","Runnob"))
#
# print("{name}网址: {site}".format(name="菜鸟教程", site="www.runnob.com"))
#
# table = {"Google": 1, "Runnob": 2, "Taobao": 3}
# for name, number in table.items():
#     print("{0:10} ===> {1:10d}".format(name, number))
#
#
# # 读取键盘输入 input()函数
# str1 = input("请输入： ")
# print("你输入的内容是：", str1)
#
# """
# 读和写文件 open() 将会返回一个 file 对象，基本语法格式如下:open(filename, mode)
# r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
# """
#
# # f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# f = open("/Users/taten/Desktop/txt.txt", "w")
# num = f.write("python是一个非常好的语言。 \n是的，的确非常好！！ \n")
# print(num)
#
# f = open("/Users/taten/Desktop/txt.txt", "r")
# str1 = f.read()
# print(str1)
#
# f = open("/Users/taten/Desktop/txt.txt", "r")
# str2 = f.readline()
# print(str2)
#
# f = open("/Users/taten/Desktop/txt.txt", "r")
# str3 = f.readlines()
# print(str3)
#
# f = open("/Users/taten/Desktop/txt.txt", "r")
# for line in f:
#     print(line, end="")
#
# # 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# f = open("/Users/taten/Desktop/txt.txt", "a+")
# value = ("www.runoob.com", 14)
# s = str(value)
# f.write(s)
#
# # f.tell()：返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
#
# """可以看到，当使用 open() 函数打开文件时，文件指针的起始位置为 0，表示位于文件的开头处，/n
# 当使用 read() 函数从文件中读取 4 个字符之后，文件指针同时向后移动了 4 个字符的位置。
# 这就表明，当程序使用文件对象读写数据时，文件指针会自动向后移动：读写了多少个数据，文件指针就自动向后移动多少个位置。
# """
# f = open("/Users/taten/Desktop/txt.txt", "r")
# print(f.tell())
# print(f.read(4))
# print(f.tell())

# f.seek() 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数;from_what 值为默认为0，即文件开头。
"""
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
"""
# f = open("/Users/taten/Desktop/txt.txt", "rb+")  # 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# # value = "0123456789abcdef"
# # num2 = f.write(value.encode())
# num2 = f.write(b"0123456789abcdef")
# print(num2)
#
#
# print(f.seek(5))
# print(f.read(1))
# print(f.seek(-3, 2))
# print(f.read(1))

with open("/Users/taten/Desktop/txt.txt", "r", encoding="utf-8") as f:
    read_data = f.read()

f.close()

# pickle 模块:python的pickle模块实现了基本的数据序列和反序列化。
