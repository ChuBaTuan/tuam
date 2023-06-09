from icecream import ic 
from tabulate import tabulate
from mysql.connector import connect
 
class QuanlySach():
    def __init__(self,db) :
        self.cur = db.cur
        self.conn = db.conn
    def them(self):
        id = input("Nhập mã sách :")
        name = input("Nhập tên sách :")
        tacgia = input("Nhập tên tác giả :")
        
        sql = "INSERT INTO books () VALUES (%s,%s,%s)"
        values = (int(id), name, tacgia)
        self.cur.execute(sql, values)
        self.conn.commit()

        print("Thêm sách thành công ")
    def sua(self):
        id = input("Nhập mã sách cần cập nhật: ")
        sql = "SELECT * FROM books WHERE id = %s"
        value = [id]
        self.cur.execute(sql, value)
        result = self.cur.fetchone()
        if result is None:
            print("Không tìm thấy sách.")
            return

        name = input("Nhập tên sách: ")
        tacgia = input("Nhập tên tác giả: ")

        sql = "UPDATE books SET name = %s, tacgia = %s WHERE id = %s"
        values = (name, tacgia, id)
        self.cur.execute(sql, values)
        self.conn.commit()

    print("Cập nhật thông tin thành công")

    def xoa(self):
        id = input("Nhập mã sách cần xóa: ")
        sql = "SELECT * FROM books WHERE id=%s"
        value = [id]
        self.cur.execute(sql, value)
        result = self.cur.fetchone()
        if result is None:
            print("Không tìm thấy sách.")
            return


        sql = "DELETE FROM books WHERE id = %s"
        value = [id]
        self.cur.execute(sql, value)
        self.conn.commit()

        print("Xoá sách thành công.")


    def timKiem(self):
        keyword = input("Nhập mã sách hoặc họ tên sách cần tìm: ")
        if self.check_id(keyword):
            id = keyword
            # Thực hiện truy vấn SELECT vào database
            sql = "SELECT * FROM books WHERE id = %s"
            value = [id]
            
        else:
            name = keyword
            # Thực hiện truy vấn SELECT vào database
            sql = "SELECT * FROM books WHERE name = %s"
            value = [name]

        self.cur.execute(sql, value)
        result = self.cur.fetchall()

        if result is None:
            print("Không tìm thấy sách.")
            return
            
        self.tabulate_print(result)
    
    def sapxep(self):
        print("Chọn tiêu chí sắp xếp:")
        print("1. Sắp xếp theo mã sách ")
        print("2. Sắp xếp theo tên sách ")
        print("3. Sắp xếp theo tác giả ")
        
        choice = input("Nhập lựa chọn của bạn (1-3): ")
        
        if choice == "1":
            sql = "SELECT * FROM books ORDER BY id ASC"
        elif choice == "2":
            sql = "SELECT * FROM books ORDER BY name ASC"
        elif choice == "3":
            sql = "SELECT * FROM books ORDER BY tacgia ASC"
        else:
            print("Lựa chọn không hợp lệ.")
            return
        
        self.cur.execute(sql)
        results = self.cur.fetchall()
        
        if not results:
            print("Không có sách trong danh mục.")
            return
        
        self.tabulate_print(results)

    def check_id(self, id):
        try:
            id = int(id)
            return True
        except:
            print("")

        return False
    
    def hienThi(self):
        print(" Danh mục sách:")
        sql = "SELECT * FROM books"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results is None:
            print("Không tìm thấy sách.")
            return
        
        self.tabulate_print(results)

    def tabulate_print(self, data):
        headers = ["Mã học viên", "Tên sách ", "Tác Giả"]
        print(tabulate(data, headers, tablefmt="grid"))



