import mysql.connector

# 配置数据库连接
config = {
    'user': 'dbconnect',
    'password': '123456',
    'host': 'zgy.myqnapcloud.com',
    'database': 'randb',
    'raise_on_warnings': True,
    'port': '7306'
}

# 创建连接
cnx = mysql.connector.connect(**config)


# 创建游标对象
cursor = cnx.cursor()

cursor.execute("insert into winno (per,red1,red2,red3,red4,red5,red6,blue) values ('2026022','15','18','23','25','28','32','11')")
cnx.commit()
# 执行查询
cursor.execute("SELECT * FROM winno")

# 获取所有结果
for row in cursor:
    print(row)

# 关闭游标和连接
cursor.close()
cnx.close()