class NhanVien:
    def __init__(self, ma_nv: str, ho_ten: str, luong: float):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong = float(luong)

    def get_thu_nhap(self) -> float:
        return self.luong
    def get_thue_thu_nhap(self) -> float:
        tn = self.get_thu_nhap()
        if tn < 9_000_000:
            return 0.0
        elif tn <= 15_000_000:
            return tn * 0.10
        else:
            return tn * 0.12

    #In ra thông tin nhân viên
    def __str__(self):
        return (f"{self.ma_nv} | {self.ho_ten} | Hành chính | "
                f"Lương: {self.luong:,.2f} | "
                f"Thu nhập: {self.get_thu_nhap():,.2f} | "
                f"Thuế: {self.get_thue_thu_nhap():,.2f}")

    def xuat(self):
        print(self.__str__())


# Lớp Tiếp Thị
class TiepThi(NhanVien):
    def __init__(self, ma_nv: str, ho_ten: str, luong: float, doanh_so: float, hoa_hong: float):
        super().__init__(ma_nv, ho_ten, luong)
        self.doanh_so = float(doanh_so)
        self.hoa_hong = float(hoa_hong)

    def get_thu_nhap(self) -> float:
        return self.luong + self.doanh_so * self.hoa_hong

    def __str__(self):
        return (f"{self.ma_nv} | {self.ho_ten} | Tiếp thị | "
                f"Lương: {self.luong:,.2f} | "
                f"Doanh số: {self.doanh_so:,.2f} | Hoa hồng: {self.hoa_hong:.2f} | "
                f"Thu nhập: {self.get_thu_nhap():,.2f} | "
                f"Thuế: {self.get_thue_thu_nhap():,.2f}")


# Lớp Trưởng Phòng
class TruongPhong(NhanVien):
    def __init__(self, ma_nv: str, ho_ten: str, luong: float, luong_trach_nhiem: float):
        super().__init__(ma_nv, ho_ten, luong)
        self.luong_trach_nhiem = float(luong_trach_nhiem)

    def get_thu_nhap(self) -> float:
        return self.luong + self.luong_trach_nhiem

    def __str__(self):
        return (f"{self.ma_nv} | {self.ho_ten} | Trưởng phòng | "
                f"Lương: {self.luong:,.2f} | "
                f"Lương trách nhiệm: {self.luong_trach_nhiem:,.2f} | "
                f"Thu nhập: {self.get_thu_nhap():,.2f} | "
                f"Thuế: {self.get_thue_thu_nhap():,.2f}")