# class Myclass():
#     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return "hello world"


# # 实例化类
# x = Myclass()
#
# print("Myclass类的属性i为：", x.i)
# print("Myclass类的方法f输出为：", x.f())
#
#
#
# class Complex():
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
#
# x = Complex(3.0, -4.5)
# print(x.r, x.i)


# # 类定义
# class people():
#     # 定义基本属性
#     name = ""
#     age = 0
#     # 定义私有属性，私有属性在类外部无法直接访问
#     __weight = 0
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s说：我 %d 岁。" % (self.name, self.age))
#
# # 实例化类
# p = people("runoob", 10, 30)
# p.speak()
#
#
# """
# 继承
# """
#
#
# #类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     #定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#
#
# class student(people):
#     gradle = ""
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name,self.age,self.grade))
#
#
# s = student("ken", 10, 60, 3)
# s.speak()
#
#
# """
# 多继承
# """
#
#
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#
# # 单继承实例
# class student(people):
#     gradle = ""
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name,self.age,self.grade))
#
#
# # 另一个类，多重继承之前的准备
# class speaker():
#     topic = ""
#     name = ""
#
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
#
#
# # 多重继承
# class sample(speaker, student):
#     a = ""
#
#     def __init__(self, n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)
#
#
# test = sample("Tim",25,80,4,"Python")
# test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
#
#
# """
# 方法重写：如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
# """
#
#
# class Parent:  # 定义父类
#     def myMethod(self):
#         print("调用父类方法")
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print("调用子类方法")
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# # super() 函数是用于调用父类(超类)的一个方法。
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法；
#
#
# """
# 类属性与方法
# 类的私有属性：__private_attrs两个下划线开头，声明该属性私有，不能在类的外部被使用或直接访问，在类内部的方法中使用self.__private
# 类的方法：在类的内部，使用def关键词在定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数，self代表类的实例。
# 类的私有方法：__private_method: 两个下划线开头，声明该方法为私有方法，只能在类的内部调用，不能在类的外部调用。self.__private_method
# """
#
#
# # 类的私有属性
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0   # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)  # 在类内部被使用
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# # 类的私有方法
# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print("name:", self.name)
#         print("url: ", self.__url)
#
#     def __foo(self):       # 私有方法
#         print("这是私有方法")
#
#     def foo(self):          # 公共方法
#         print("这是公共方法")
#
#
# x = Site("菜鸟教程", "www.runoob.com")
# x.who()
# x.foo()
# x.__foo()

"""
类的专用方法
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
"""

"""
运算符重载：Python同样支持运算符重载，我们可以对类的专有方法进行重载
"""


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector %d %d" %(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
