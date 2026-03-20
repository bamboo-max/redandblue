import mysql.connector
from mysql.connector import Error


class MySQLDB:
    def __init__(self, host_name="localhost", user_name="root", user_password="password", db_name="testdb",db_port="3306"):
        self.conn = None
        try:
            self.conn = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password, database=db_name,port=db_port)
            if self.conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def create_table(self, create_table_sql):
        self.execute(create_table_sql)

    def insert(self, insert_sql, data):
        try :
            self.execute(insert_sql, data)
            return self.cursor.lastrowid  # 获取最后插入行的ID（如果适用）
        except Error as e:
            return 0
            print(e)


    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print('Connection closed.')
        else:
            print('No connection to close.')