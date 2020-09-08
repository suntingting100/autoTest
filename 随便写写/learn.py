# import keyword
# print(keyword.kwlist)
#
# # print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""; sys.stdout.write() =print(, end="")
# import sys
# sys.stdout.write('hello')
# sys.stdout.write('hello')
# print("hello")
# print("hello")
#
# # Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
# a = 1
#
# while a < 7:
#     if (a % 2 == 0):
#         print(a, "is even")
#     else:
#         print(a, "is odd")
#     a += 1
#
# # if的基本用法
# flag = False
# name = "luren"
#
# if name == "python":
#     flag = True
#     print("welcome boss")
# else:
#     print(name)
#
# num = 5
# if num == 3:
#     print("boss")
# elif num == 2:
#     print("user")
# elif num == 1:
#     print("worker")
# elif num < 0:
#     print("error")
# else:
#     print("roadman")
#
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print("Name的值为：%s" % dict.get("Name"))
#
# print(dict.keys())
# print(dict.items())
# print(dict.values())
#
#
# dict.clear()
# print(dict)

# 用字典记录学生名字和分数，再分级:
# students = {}
# write = 1
# while write:
#     name = str(input("请输入你的名字： "))
#     grade = int(input("请输入你的学分： "))
#     students[str(name)] = grade
#     write = int(input("继续输入？ \n  1/继续 0/退出" ))
# print("name  rate".center(20, "-"))
# for key, value in students.items():
#     if value > 90:
#         print("%s %s A".center(20, "-") % (key,value))
#     elif 90 < value <= 60:
#         print("%s %s B".center(20, "-") % (key,value))
#     else:
#         print("%s %s C".center(20, "-") % (key,value))
#
# # 获取字典中最大的值
# prices = {
#     "A": 123,
#     'B': 450.1,
#     'C': 12,
#     'E': 444,
# }
#
# print(list(prices.values()))
#
# max_price = max(zip(prices.values(), prices.keys()))
# print(max_price)

# # 通过 values 取到 key 的方法
# dict = {"a": 1, "b": 2, "c": 3}
# print(list(dict.values()))
# print(list(dict.keys())[list(dict.values()).index(1)])






