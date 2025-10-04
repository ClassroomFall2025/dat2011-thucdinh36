# Code lab 4 bài 1 ở đây
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc<= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <=30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc




# Code lab 4  bài 2 ở đây
def tinh_nguyen_lieu(sl_dx, sl_thcam, sl_bdeo):
    banh_dau_xanh = {"duong": 0.04, "dau": 0.07}
    banh_thap_cam = {"duong": 10.00, "dau": 0}
    banh_deo = {"duong": 0.05, "dau": 0.02}
    nguyen_lieu = {}
    duong_hop_banh = sl_dx * banh_dau_xanh["duong"] + sl_thcam * banh_thap_cam["duong"] + sl_bdeo * banh_deo["duong"]
    dau_hop_banh = sl_dx * banh_dau_xanh["dau"] + sl_thcam * banh_thap_cam["dau"] + sl_bdeo * banh_deo["dau"]
    nguyen_lieu["duong"] = duong_hop_banh
    nguyen_lieu["dau"] = dau_hop_banh
    return nguyen_lieu
