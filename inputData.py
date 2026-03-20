from os.path import split

from MySqlDB import MySQLDB


host_name="zgy.myqnapcloud.com"
user_name="dbconnect"
user_password="123456"
db_name="randb"
db_port = '7306'

db = MySQLDB(host_name,user_name,user_password,db_name,db_port)

per = input("期号：")
red = input("红球：")
redlist = red.split(",")

print(len(redlist))

exit()
iid = 0
iid = db.insert('INSERT INTO winno (per,red1,red2,red3,red4,red5,red6,blue) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (per,'15','18','23','25','28','32','11'))


if iid != 0 :
    print(f"新的数据id={iid}")
else:
    print("插入失败")