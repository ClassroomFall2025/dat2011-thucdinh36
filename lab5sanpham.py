class SanPham1:
    def __init__(self):
        self.ten_sp = ""
        self.gia = 0
        self.giam_gia = 0

    def thue_nhap_khau(self):
        return self.gia * 0.1

    def nhap(self):
        self.ten_sp = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.giam_gia = float(input("Nhập giảm giá: "))

    def xuat(self):
        print("\n--- Thông tin sản phẩm ---")
        print(f"Tên sản phẩm: {self.ten_sp}")
        print(f"Giá: {self.gia:,.0f}")
        print(f"Giảm giá: {self.giam_gia:,.0f}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau():,.0f}")
        print("--------------------------")



class SanPham2:
    def __init__(self):
        self.__ten_sp = ""
        self.__gia = 0
        self.__giam_gia = 0

    # Getter / Setter
    def get_ten_sp(self):
        return self.__ten_sp
    def set_ten_sp(self, ten_sp):
        self.__ten_sp = ten_sp
    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia
    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.__gia * 0.1

    def nhap(self):
        self.__ten_sp = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá: "))

    def xuat(self):
        print("\n--- Thông tin sản phẩm ---")
        print(f"Tên sản phẩm: {self.__ten_sp}")
        print(f"Giá: {self.__gia:,.0f}")
        print(f"Giảm giá: {self.__giam_gia:,.0f}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau():,.0f}")
        print("--------------------------")



class SanPham3:
    def __init__(self, ten_sp="", gia=0, giam_gia=0):
        self.__ten_sp = ten_sp
        self.__gia = gia
        self.__giam_gia = giam_gia

    # Getter / Setter
    def get_ten_sp(self):
        return self.__ten_sp
    def set_ten_sp(self, ten_sp):
        self.__ten_sp = ten_sp
    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia
    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.__gia * 0.1

    def nhap(self):
        self.__ten_sp = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá: "))

    def xuat(self):
        print("\n--- Thông tin sản phẩm ---")
        print(f"Tên sản phẩm: {self.__ten_sp}")
        print(f"Giá: {self.__gia:,.0f}")
        print(f"Giảm giá: {self.__giam_gia:,.0f}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau():,.0f}")
        print("--------------------------")