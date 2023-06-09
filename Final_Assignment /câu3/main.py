from quanly.Books import QuanlySach
from quanly.DB import QuanLyDB
from quanly.Menu import Menu


def xuly(qls):
    while True:
        menu.menu()
        choice = input("Nhập lựa chọn của bạn (0-5): ")
        if choice == "0":
            print("Trở về")
            break
        elif choice == "2": 
            print("Thêm sách")
            qls.them()

        elif choice == "3":  
            print("Cập nhật thông tin sách")
            qls.sua()
        elif choice == "4":  
            print("Xóa thông tin sách")
            qls.xoa()
        elif choice == "5": 
            print("Tìm kiếm sách")
            qls.timKiem()
        elif choice == "1": 
            print(" Danh mục sách")
            qls.hienThi()
        elif choice == "6": 
            print(" Sắp xếp sách")
            qls.sapxep()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__" :
    menu = Menu()
    db = QuanLyDB()
    name_db = 'tuan89_database'
    # db.delete_DB(name_db)
    if not db.check_database_exists(name_db) :        
        db.create_DB(name_db)
        db.ceate_table(name_db)
    else:
        db.connect_DB(name_db)

    qls = QuanlySach(db)
    xuly(qls)
    db.close_db()


    