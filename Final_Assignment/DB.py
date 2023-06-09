import mysql.connector

class QuanLyDB():
    def __init__(self):
        self.my_user="root" 
        self.my_password="root"
        self.conn = mysql.connector.connect(
            host="localhost",
            user=self.my_user,
            password=self.my_password
        )
        self.cur = self.conn.cursor()
        
    def check_database_exists(self, database_name):
        self.cur.execute("SHOW DATABASES")
        databases = self.cur.fetchall()
        for db in databases:
            if db[0] == database_name:
                return True
        return False
    
    def create_DB(self, name):
        self.cur.execute(f"CREATE DATABASE {name}")

    def delete_DB(self, name):
        self.cur.execute(f"DROP DATABASE IF EXISTS {name}")

    def connect_DB(self, name):
        self.conn = mysql.connector.connect(
            host="localhost",
            user=self.my_user,
            password=self.my_password,
            database=name
        )
        # Tạo con trỏ để thực hiện các truy vấn
        self.cur = self.conn.cursor()

    def ceate_table(self, name):
        self.connect_DB(name)
        
        # Tạo bảng "students"
        self.cur.execute("""
            CREATE TABLE books (
                id INT PRIMARY KEY,
                name VARCHAR(255),
                tacgia VARCHAR(15)
            )
        """)

        # Tạo con trỏ để thực hiện các truy vấn
        self.cur = self.conn.cursor()
    
    def close_db(self):
        self.conn.close()