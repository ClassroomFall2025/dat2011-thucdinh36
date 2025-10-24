from sinhvienpoly import *

class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def nhap_dssv(self):
        while True:
            ho_ten = input("Nhập họ tên sinh viên (hoặc '0' để dừng): ")
            if ho_ten == "0":
                print("Kết thúc nhập.")
                break

            nganh = input("Nhập ngành học (IT/Biz): ").strip().lower()
            if nganh == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm HTML: "))
                css = float(input("Điểm CSS: "))
                sv = SinhVienIT(ho_ten, java, html, css)
            elif nganh == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = SinhVienBiz(ho_ten, marketing, sales)
            else:
                print("Ngành không hợp lệ, vui lòng nhập lại.")
                continue

            self.dssv.append(sv)

    def xuat_dssv(self):
        if not self.dssv:
            print("Danh sách trống.")
        else:
            print("\n--- DANH SÁCH SINH VIÊN ---")
            for sv in self.dssv:
               sv.xuat()

    def xuat_dssv_gioi(self):
        sv_gioi = [sv for sv in self.dssv if sv.get_diem() >= 8]
        if not sv_gioi:
            print("Không có sinh viên giỏi.")
        else:
            print("\n--- SINH VIÊN CÓ HỌC LỰC GIỎI ---")
            for sv in sv_gioi:
                sv.xuat()

    def sap_xep_dssv(self):
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("Đã sắp xếp danh sách sinh viên theo điểm giảm dần.")
        for sv in self.dssv:
                sv.xuat()
