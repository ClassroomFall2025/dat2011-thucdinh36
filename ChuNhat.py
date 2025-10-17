class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def get_chu_vi(self):
        return 2 * (self.dai + self.rong)
    def get_dien_tich(self):
        return self.dai * self.rong
    def xuat(self):
        print(f"Chiều dài: {self.dai}, Chiều rộng: {self.rong}")
        print(f"Diện tích: {self.get_dien_tich()}, Chu vi: {self.get_chu_vi()}")

class Vuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
    def xuat(self):
        print(f"Cạnh hình vuông: {self.dai}")
        print(f"Diện tích: {self.get_dien_tich()}, Chu vi: {self.get_chu_vi()}")

cn1 = ChuNhat(4, 6)
cn2 = ChuNhat(3, 5)
vu = Vuong(4)

cn1.xuat()
cn2.xuat()
vu.xuat()