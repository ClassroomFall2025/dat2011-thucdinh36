class SinhVienPoly:
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh

    # Phương thức trừu tượng (chưa có cách tính)
    def get_diem(self):
        pass

    # Tự động xếp học lực dựa trên điểm
    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    # Xuất thông tin sinh viên
    def xuat(self):
        print(f"Họ tên: {self.ho_ten}, Ngành: {self.nganh}, "
              f"Điểm: {self.get_diem():.2f}, Học lực: {self.get_hoc_luc()}")


# Lớp SinhVienIT kế thừa SinhVienPoly
class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh, java, html, css):
        super().__init__(ho_ten, nganh)
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4


# Lớp SinhVienBiz kế thừa SinhVienPoly
class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, marketing, sales):
        super().__init__(ho_ten, nganh)
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3