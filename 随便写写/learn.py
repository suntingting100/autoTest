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
"""
if的基本用法
"""
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


"""
条件控制
简单的 if 判断实例： 因为0和null都相当于是false
"""

# var1 = 100
# if var1:
#     print("1 - if 表达式条件为true")
#     print(var1)
#
# var2 = 0
# if var2:
#     print("2 - if 表达式条件为true")
#     print(var2)
# print("Good bye")

# 实例演示了狗的年龄计算判断：

# age = int(input("请输入你家狗的年龄： "))
# print("")
# if age <= 0:
#     print("你是在逗我吧")
# elif age == 1:
#     print("相当于14岁的人")
# elif age == 2:
#     print("相当于22岁的人")
# elif age > 2:
#     human = 22 + (age-2)*5
#     print("对应人的年龄 %d" % human)
#
# input("点击 enter 健退出")

"""
数字的比较运算
"""
# number = 7
# guess = -1
# print("数字猜谜语游戏")
# while guess != number:
#     guess = int(input("请输入你猜的数字： "))
#     if guess == number:
#         print("恭喜你猜对了")
#     elif guess < number:
#         print("猜的数字太小了")
#     elif guess > number:
#         print("猜的数字太大了")
# input("点击 enter 结束")

"""
if 嵌套实例
"""
# num = int(input("输入一个数字： "))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("你的数字可以整除2和3")
#     else:
#         print("你的数字可以整除2，但不可以整除3")
# else:
#     if num % 3 == 0:
#         print("你的数字可以整除3，但不可以整除2")
#     else:
#         print("你的数字不能整除2，也不能整除3")


"""
while循环
Python中的循环语句有for 和 while
"""
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum += counter
#     counter += 1
#
# print("1 到 %d 之间的和为：%d" % (n, sum))


# 无限循环
# var = 1
# while var == 1:
#     num = int(input("输入一个数字： "))
#     print("你输入的数字是：%d" % num)
# print("Good bye")

"""
while 循环使用 else 语句
"""
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于等于5")


"""
for 语句
"""
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

"""
 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
"""

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程")
        break
    print("循环数据 " + site)

else:
    print("完成循环")








