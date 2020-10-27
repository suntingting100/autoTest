class Myclass():
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return "hello world"


# 实例化类
x = Myclass()

print("Myclass类的属性i为：", x.i)
print("Myclass类的方法f输出为：", x.f())



class Complex():
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


# 类定义
class people():
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s说：我 %d 岁。" % (self.name, self.age))

# 实例化类
p = people("runoob", 10, 30)
p.speak()


"""
继承
"""
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))


class student(people):
    gradle = ""
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name,self.age,self.grade))


s = student("ken", 10, 60, 3)
s.speak()


"""
多继承
"""
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

# 单继承实例
class student(people):
    gradle = ""
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name,self.age,self.grade))

# 另一个类，多重继承之前的准备
class speaker():
    topic = ""
    name = ""
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

# 多重继承
class sample(speaker, student):
    a = ""
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim",25,80,4,"Python")
test.speak()





