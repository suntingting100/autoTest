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

"""
通过 values 取到 key 的方法
"""
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
# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print(x)

"""
 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
"""
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程")
#         break
#     print("循环数据 " + site)
#
# else:
#     print("完成循环")

"""
range()函数
"""
# for i in range(5):
#     print(i, end="、")
#
# for i in range(5, 9):
#     print(i)
#
# for i in range(0, 10, 3):
#     print(i)
#
# for i in range(-10, -100, -30):
#     print(i)
#
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])
#
# print(list(range(5)))


"""
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
"""
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print("循环结束。")
#
#
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print("循环结束")

"""
更多实例
"""
# for letter in "Runoob":
#     if letter == "b":
#         break
#     print("当前字母为：", letter)
#
# var = 10
# while var > 0:
#     print("当前变量值为：", var)
#     var = var - 1
#     if var == 5:
#         break
# print("Good bye!")
#
#
# for letter in "Runoob":
#     if letter == "o":
#         continue
#     print("当前字母：", letter)
#
# var = 10
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print("当前变量值为：", var)
# print("Good bye")

"""
1、如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
2.如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行！
"""

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         print(n, "是质数")

"""
pass语句
"""
# for letter in "Runoob":
#     if letter == "o":
#         pass
#         print("执行pass块")
#     print("当前字母为：", letter)
# print("Good bye")


# sequence = [12, 34, 34, 23, 45, 76, 89]
# for i, j in enumerate(sequence):
#     print(i, j)
#
# for i in range(1,6):
#    for j in range(1, i+1):
#       print("*",end='')
#    print('\r')

"""
迭代器有两个基本的方法：iter() 和 next()。
"""
# list = [1, 2, 3, 4]
# it = iter(list)   # 创建迭代器对象
# print(next(it))   # 输出迭代器的下一个元素
# print(next(it))
#
# list = [1, 2, 3, 4]
# it = iter(list)
# for x in it:
#     print(x, end=" ")

# import sys
#
# list = [1, 2, 3, 4]
# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


"""
每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""
# import sys
#
#
# def feibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a+b
#         counter += 1
#
#
# f = feibonacci(10)
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


"""
函数
"""
# def hello():
#     print("hello world")
# hello()


# def changeme(mylist):
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值：", mylist)
#     return
#
#
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值：", mylist)

"""
加了星号 * 的参数会以元组(tuple)的形式导入;如果在函数调用时没有指定参数，它就是一个空元组
加了两个星号 ** 的参数会以字典的形式导入。
声明函数时，参数中星号 * 可以单独出现;如果单独出现星号,「 * 后的参数」必须用关键字传入
"""


# def f(a, b, *, c):
#     return a+b+c
# print(f(1, 2, c=3))

"""
python使用lambda来创建匿名函数: lambda 函数的语法只包含一个语句
"""


# 列表
"""
list.append(x):把一个元素添加到列表的结尾
list.extend(L):通过添加指定列表的所有元素来扩充列表
list.insert(i, x):在指定位置插入一个元素
list.remove(x):删除列表中值为 x 的第一个元素
list.pop([i]):从列表的指定位置移除元素，并将其返回
list.clear():移除列表中的所有项
list.index(x):返回列表中第一个值为 x 的元素的索引
list.count(x):返回 x 在列表中出现的次数。
list.sort():对列表中的元素进行排序。
list.reverse():倒排列表中的元素。
list.copy():返回列表的浅复制
"""

"""
将列表当做堆栈使用
将列表当作队列使用
"""


"""
 Python 内建数据类型是字典
"""
# tel = {'jack': 4098, 'sape': 4139}
# tel["guido"] = 4127
# print(tel)
# print(tel['jack'])
#
# del tel['sape']
# print(tel)
# tel["irv"] = 4127
# print(tel)
#
# print(list(tel.keys()))
# print(sorted(tel.keys()))
#
# "guido" in tel
# "jack" not in tel

# 构造函数 dict() 直接从键值对元组列表中构建字典

# a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(a)
#
# # 字典推导可以用来创建任意键和值的表达式词典：
# a = {x: x**2 for x in (2, 4, 6)}
# print(a)
#
# # 关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
# a = dict(sape=4139, guido=4127, jack=4098)
# print(a)

"""
遍历技巧:
"""
# # 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
#
# # 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)
#
# # 同时遍历两个或更多的序列，可以使用 zip() 组合
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(q, a)
#
# # 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
# for i in reversed(range(1, 10, 2)):
#     print(i)
#
# # 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)


"""
模块
"""
# import sys
#
# print("命令参数如下：")
# for i in sys.argv:
#     print(i)
#
# print("\n\n python路径为：", sys.path, "\n")

# import support
#
# support.print_func("Runnob")

# __name__属性
if __name__ == "__main__":
    print("程序自身运行")
else:
    print("我来自另一模块")























