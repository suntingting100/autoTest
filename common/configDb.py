# 这个文件主要编写数据库连接池的相关内容

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "user", "pwd")

# 使用cursor（）的方法获取操作游标
cursor = db.cursor()

# SQL语句查询
sql = "select * from employee" \
      " where income > %s" % (1000)

try:
    # 执行语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]

        # 打印结果
        print(("fname=%s, lname=%s, age=%s, sex=%s, income=%s" %(fname, lname, age, sex, income))
except:
    print("Error:unable to fetch data")

# 关闭数据库
db.close()
