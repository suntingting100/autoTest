#
# # 列出列表中有多少个正数，多少个负数
# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8, 76]
#
# b = [i for i in a if i > 0]
# print("大于0的个数为：%s" %len(b))
# print("小于0的个数为：%s" %(len(a) - len(b)))
#
#
# # 字符串切片 字符串axbyczdj，如何得到结果 abcd
# a = "axbyczdj"
# b = a[::2]
# print(b)
#
# # 格式化输出 已知一个数字1，如何输出0001
# a = 1
# print("%04d" % a)

# 队列 已知一个队列，如：[1, 3, 5, 7]，如何把第1个数字放到第三个位置变成[3,5,1,7]
# a = [1, 3, 5, 7]
# a.insert(3, a[0])
# print(a[1:])

# 交换 a，b的值
# a = 8
# b = 9
# a, b = b, a
# print(a)
# print(b)

#  水仙花 打印出100-999所有的水仙花数，水仙花是指1个三位数，其各位数的立方和等于该数本身，例如153 = 1三次方 + 5的三次方 + 3的三次方
# a = []
# for i in range(100, 999):
#     s = 0
#     m = list(str(i))
#     for j in m:
#         s += int(j)**len(m)
#     if i == s:
#         print(i)
#         a.append(i)
# print("100-999所有的水仙花数: %s" % a)


# 完全数：一个数完全等于他的因子之和；例如第一个完全数是6，他有约数1、2、3、6；除去他本身6外，其余3个数相加
# a = []
# for i in range(1, 1000):
#     s = 0
#     for j in range(1, i):
#         if i % j ==0 and j < i:
#             s += j
#     if s == i:
#         print(s)
#         a.append(s)
# print("1000以内的完全数 %s" % a)


# 排序 冒泡排序
# a = [1, 3, 10, 9, 21, 35, 4, 6]
# s = range(1, len(a))[::-1]
# print(list(s))
#
# for i in s:
#     for j in range(1, i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#     print("第%s 轮交换后数据：%s" %(len(s)-i+1, a))
# print(a)


# # 排序 从小到大；从大到小；去重 [1, 3, 6, 9, 7, 3, 4, 6]
# a= [1, 3, 6, 9, 7, 3, 4, 6]
# a.sort()
# print(a)
#
# a.sort(reverse=True)
# print(a)
#
# b = list(set(a))
# print(b)

# 计算n的阶乘
