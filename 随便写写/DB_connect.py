import pymysql

db = pymysql.connect("rm-2ze2n29o0j4r4z3kp1o.mysql.rds.aliyuncs.com", "game_dev", "i2v5dO#OTNUbqRQR", "game_dev")

cursor = db.cursor()

sql = "select * from trade_order where startTime between '2020-08-25 00:00:00' and '2020-08-25 23:59:59'"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        userId = row[1]
        orderNo = row[2]
        status = row[12]

        print("id=%s, userId=%s, orderNo=%s, status=%d" % (id, userId, orderNo, status))

except:
    print("Error, unable to fetch data")

db.close()

