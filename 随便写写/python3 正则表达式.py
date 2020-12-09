"""
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
"""

"""
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
"""
import re
print(re.match("www", "www.runoob.com").span())    # 在起始位置匹配
print(re.match("com", "www.runoob.com"))     # 不在起始位置匹配


line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
else:
    print("No match!!")


"""
re.search 扫描整个字符串并返回第一个成功的匹配。
"""
print(re.search("www", "www.runoob.com").span())  # 在起始位置匹配
print(re.search("com", "www.runoob.com").span())   # 不在起始位置匹配

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
else:
    print("Nothing found")


"""
re.match与re.search的区别
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None，而 re.search 匹配整个字符串，直到找到一个匹配。
"""

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r"dogs", line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group()", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r"dogs", line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group()", matchObj.group())
else:
    print("Nothing found")

"""
检索和替换
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
"""
import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r"#.*$", "", phone)
print("电话号码：", num)

# 移除非数字内容
num = re.sub(r"\D", "", phone)
print("电话号码：", num)

"""
repl 参数是一个函数
"""
# 将匹配到的数字*2

def double(matched):
    value = int(matched.group("value"))
    return str(value * 2)


s = "A23G4HFD567"

print(re.sub("(?P<value>\d+)", double, s))


"""
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
"""




