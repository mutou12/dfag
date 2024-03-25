#  -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2024 , Inc. All Rights Reserved
#  #
#  @Time    : 2024/3/25 21:38
#  @Author  : 赫凯
#  @Email   : hekaiiii@163.com
#  @File    : connect.py
#  @Software: PyCharm


import psycopg2

# 数据库连接参数
db_params = {
    "dbname": "pgstudy",
    "user": "postgres",
    "password": "abc",
    "host": "localhost",  # 默认是localhost，如果不是，请替换为你的数据库服务器地址
    "port": "5432"  # 默认端口是5432，如果不是，请替换为你的数据库端口
}
# 建立连接
try:
    conn = psycopg2.connect(**db_params)
    print("Connected to the database successfully.")
except psycopg2.Error as e:
    print("Unable to connect to the database.")
    print(e)

# 创建一个游标对象
cur = conn.cursor()

# 执行查询
try:
    # 例如，查询数据库中的所有表
    cur.execute("SELECT * FROM employees;")
    records = cur.fetchall()
    for record in records:
        print(record)
except psycopg2.Error as e:
    print("Error in cursor.execute(), ", e)

# 关闭游标和连接
cur.close()
conn.close()