import keyword
print(keyword.kwlist)

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""; sys.stdout.write() =print(, end="")
import sys
sys.stdout.write('hello')
sys.stdout.write('hello')
print("hello")
print("hello")

for i in sys.argv: