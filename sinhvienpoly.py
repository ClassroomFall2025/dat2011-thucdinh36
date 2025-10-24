class SinhVienPoly:
    def __init__(self, ho_ten, nganh_hoc):
        self.ho_ten = ho_ten
        self.nganh_hoc = nganh_hoc

    def get_diem(self):
        pass

    def get_hoc_luc(self):
        diem = self.get_diem()
        if 9 <= diem <= 10:
            return "Xuất sắc"
        elif diem >= 8:
            return "Giỏi"
        elif diem >= 7:
            return "Khá"
        elif diem >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"{self.ho_ten}, {self.nganh_hoc}, Điểm TB: {self.get_diem():.2f}, Học lực: {self.get_hoc_luc()}"
    def xuat(self):
        print(f"{self.ho_ten}, {self.nganh_hoc}, Điểm TB: {self.get_diem():.2f}, Học lực: {self.get_hoc_luc()}")


class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, "IT")
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css

    def get_diem(self):
        return (self.diem_java * 2 + self.diem_html + self.diem_css) / 4


class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, diem_marketing, diem_sales):
        super().__init__(ho_ten, "Biz")
        self.diem_marketing = diem_marketing
        self.diem_sales = diem_sales

    def get_diem(self):
        return (self.diem_marketing * 2 + self.diem_sales) / 3