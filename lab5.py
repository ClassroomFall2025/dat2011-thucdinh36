#class SanPham:
    #def __init__(self, ten_san_pham, gia, giam_gia):
        #self.__ten_san_pham = ten_san_pham
        #self.__gia = gia
        #self.__giam_gia = giam_gia

    #def thue_nhap_khau(self):
     #   return self.gia * 0.1

    #def nhap_sp(self):
     #   self.ten_san_pham = input("Tên sản phẩm: ")
      #  self.gia = float(input("Giá: "))
 #       self.giam_gia = float(input("Giảm giá: "))

#    def xuat_tt_sp(self):
 #       print(f"Sản phẩm {self.ten_san_pham} có giá {self.gia:,.0f} và được giảm giá {self.giam_gia}")
  #      print(f"Thuế nhập khẩu (10%): {self.thue_nhap_khau():,.0f}")



#class SanPham:
    #def __init__(self, ten_san_pham,gia, giam_gia):
        
        #self.__ten_san_pham = ten_san_pham
        #self.__gia = gia
        #self.__giam_gia = giam_gia

    #def get_ten_san_pham(self):
       # return self.__ten_san_pham
    #def set_ten_san_pham(self, ten):
      #  self.__ten_san_pham = ten
    #def get_gia(self):
    #    return self.__gia
    #def set_gia(self, gia):
    #    self.__gia = gia
    #def get_giam_gia(self):
       # return self.__giam_gia
   #def set_giam_gia(self, giam_gia):
       # self.__giam_gia = giam_gia
    
    #def thue_nhap_khau(self):
       # return self.__gia * 0.1

    #def xuat_tt_sp(self):
       # print(f"Sản phẩm {self.__ten_san_pham} có giá {self.__gia} và giảm {self.__giam_gia}")
       # print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")



class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia

    def thue_nhap_khau(self):
        return self.__gia * 0.1

    def xuat_tt_sp(self):
        print("\n--- Thông tin sản phẩm ---")
        print(f"Tên sản phẩm: {self.__ten_san_pham}")
        print(f"Giá: {self.__gia}")
        print(f"Giảm giá: {self.__giam_gia}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")

# Tạo 2 sản phẩm bằng hàm khởi tạo
if __name__ == "__main__":
    sp1 = SanPham("Laptop Dell", 20000000, 1500000)
    sp2 = SanPham("Điện thoại Samsung", 15000000, 1000000)

    sp1.xuat_tt_sp()
    sp2.xuat_tt_sp()