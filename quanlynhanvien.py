from nhanvien import *
from typing import List, Optional

class QuanLyNhanVien:
    def __init__(self):
        self.dsnv: List[NhanVien] = []

# Y1 Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file
    def nhap_dsnv(self):
        print("=== NHẬP DANH SÁCH NHÂN VIÊN ===")
        while True:
            ma = input("Nhập mã nhân viên (hoặc '0' để dừng): ").strip()
            if ma == "0":
                print("Kết thúc nhập.")
                break

            ho_ten = input("Nhập họ tên: ").strip()
            loai_nhan_vien = input("Loại nhân viên (1-Hành chính, 2-Tiếp thị, 3-Trưởng phòng): ").strip()

            try:
                if loai_nhan_vien == "1":
                    luong = float(input("Lương: "))
                    nv = NhanVien(ma, ho_ten, luong)
                elif loai_nhan_vien == "2":
                    luong = float(input("Lương: "))
                    doanh_so = float(input("Doanh số: "))
                    hoa_hong = float(input("Hoa hồng (vd 0.05): "))
                    nv = TiepThi(ma, ho_ten, luong, doanh_so, hoa_hong)
                elif loai_nhan_vien == "3":
                    luong = float(input("Lương: "))
                    luong_tn = float(input("Lương trách nhiệm: "))
                    nv = TruongPhong(ma, ho_ten, luong, luong_tn)
                else:
                    print("Loại nhân viên không hợp lệ. Nhập lại.")
                    continue
            except ValueError:
                print("Dữ liệu nhập không hợp lệ. Nhập lại.")
                continue

            self.dsnv.append(nv)
            print(f"Đã thêm: {nv}")

# Y2 Đọc và xuất danh sách nhân viên ra màn hình.
    def xuat_dsnv(self):
        if not self.dsnv:
            print("Danh sách nhân viên trống.")
            return
        print("\n=== DANH SÁCH NHÂN VIÊN ===")
        for nv in self.dsnv:
            print(nv)

    #Y3 Tìm và hiển thị nhân viên theo mã
    def tim_theo_ma(self, ma: str) -> Optional[NhanVien]:
        for nv in self.dsnv:
            if nv.ma_nv == ma:
                print("Tìm thấy:", nv)
                return nv
        print("Không tìm thấy nhân viên có mã:", ma)
        return None
    
    #Y4 Xóa nhân viên theo mã nhập từ bàn phím
    def xoa_theo_ma(self, ma: str):
        for nv in self.dsnv:
            if nv.ma_nv == ma:
                self.dsnv.remove(nv)
                print("Đã xóa nhân viên:", nv.ho_ten)
                return
        print("Không tìm thấy nhân viên cần xóa.")
    #Y5 Cập nhật thông tin nhân viên theo mã 
    def cap_nhat_theo_ma(self,ma: str):
        nv = self.tim_theo_ma(ma)
        if nv:
            print("Nhập thông tin mói(bỏ trống nếu không thay đổi):")
            ten_moi = input(f"họ tên({nv.ho_ten}): ").strip()
            if ten_moi:
                nv.ho_ten = ten_moi
                luong_moi= input(f"Lương({nv.luong}):").strip()
                if luong_moi:
                    nv.luong = float(luong_moi)
                print("Lương nhập không hợp lệ.")
            print("Cập nhật thành công")
    #Y6 Tìm các nhân viên theo khoảng lương
    def tim_theo_khoang_luong(self, min_1: float, max_1: float):
        ket_qua = [nv for nv in self.dsnv if min_1 <= nv.get_thu_nhap() <=max_1]
        if ket_qua:
            print(f"\n== Nhân viên có thu nhập trong[{min_1}, {max_1}] ==")
            for nv in ket_qua:
                print(nv)
        else:
            print("Không tìm thấy nhân viên trong khoảng thu nhập này.")
    #Y7 Sắp xếp nhân viên theo họ và tên
    def sap_xep_theo_ten(self):
        self.dsnv.sort(key=lambda nv: nv.ho_ten)
        print("Đã sắp xếp theo họ tên.")
    #Y8 Sắp xếp nhân viên theo thu nhập
    def sap_xep_theo_thu_nhap(self):
        self.dsnv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
        print("Đã sắp xếp theo thu nhập giảm dần.")
    #Y9 Xuất 5 nhân viên có thu nhập cao nhất
    def top_5_thu_nhap(self):
        top5 = sorted(self.dsnv, key=lambda nv: nv.get_thu_nhap(), reverse=True)[:5]
        print("\n== TOP 5 NHÂN VIÊN CÓ THU NHẬP CAO NHẤT ==")
        for nv in top5:
            print(nv)


        


    
        

