# # var1是全局名称
# var1 = 5
# def some_func():
#
#     var2 = 6       # # var2是局部名称
#     def some_inner_func():
#         var3 = 7        # # var2是内嵌局部名称

"""
有四种作用域：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。

L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索
"""
import builtins
print(dir(builtins))

"""
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
"""
# if True:
#     msg = "I am from Runoob"
#
# print(msg)
#
# # 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
# def test():
#     msg_inner = "I am from Runoob"
#
# print(msg_inner)


"""
全局变量和局部变量
"""
# total = 0
#
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数内是局部变量：", total)
#     return total
#
# sum(10, 20)
# print("函数外是全局变量：", total)

"""
global 和 nonlocal关键字:当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
"""
# # 修改全局变量 num
# num = 1
# def fun1():
#     global num
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)
#
# # 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

a = 10
def test():
    global a        # 修改 a 为全局变量：
    a += 1
    print(a)
test()

a = 1
def test(a):        # 通过函数参数传递
    a += 1
    print(a)
test(a)



