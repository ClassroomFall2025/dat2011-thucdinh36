import sinhvienpoly as svpl

class QuanLySinhVien:
    # khởi tạo danh sách sinh viên ban đầu rỗng
    def __init__(self):
        self.dssv = []

    # phương thức nhập danh sách sinh viên
    def nhap_danh_sach_sinh_vien(self):
        while True:
            ho_ten_sv = input("Nhập họ tên sinh viên: ")
            nganh_hoc = input("Nhập ngành học sinh viên: ")

            if nganh_hoc.lower() == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm HTML: "))
                css = float(input("Điểm CSS: "))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, java, html, css)
                self.dssv.append(sv)

            elif nganh_hoc.lower() == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = svpl.SinhVienBiz(ho_ten_sv, nganh_hoc, marketing, sales)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "exit":
                print("Kết thúc nhập thông tin sinh viên.")
                break
            else:
                print("Ngành học không hợp lệ! Vui lòng nhập lại.")

        return self.dssv
   

    def Xuat_danh_sach_sinh_vien(self):
        pass

    def xuat_dssv_gioi(self):
        pass

    def sap_xep_dssv(self):
        pass