import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='0222', db='testmysql', charset='utf8')
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回收影响行数

effect_row = cursor.execute("select * from test1")
print(effect_row)

# 获取剩余结果的第一行数据
rows = cursor.fetchall()

for item in rows:
    print(item)
