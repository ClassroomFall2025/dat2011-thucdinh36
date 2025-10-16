def menu():
    print("\n=== MENU QUẢN LÝ NHÂN SỰ ===")
    print("1. Nhập danh sách nhân viên")
    print("2. Xuất danh sách nhân viên")
    print("3. Tìm nhân viên theo mã")
    print("4. Xóa nhân viên theo mã")
    print("5. Cập nhật thông tin nhân viên")
    print("6. Tìm nhân viên theo khoảng lương")
    print("7. Sắp xếp nhân viên theo họ và tên")
    print("8. Sắp xếp nhân viên theo thu nhập")
    print("9. Xuất 5 nhân viên có thu nhập cao nhất")
    print("0. Thoát")

    chon = input("Nhập lựa chọn của bạn: ")

    if chon == "1":
        print(">>> Nhập danh sách nhân viên")
    elif chon == "2":
        print(">>> Xuất danh sách nhân viên")
    elif chon == "3":
        print(">>> Tìm nhân viên theo mã")
    elif chon == "4":
        print(">>> Xóa nhân viên theo mã")
    elif chon == "5":
        print(">>> Cập nhật thông tin nhân viên")
    elif chon == "6":
        print(">>> Tìm nhân viên theo khoảng lương")
    elif chon == "7":
        print(">>> Sắp xếp nhân viên theo họ và tên")
    elif chon == "8":
        print(">>> Sắp xếp nhân viên theo thu nhập")
    elif chon == "9":
        print(">>> Xuất 5 nhân viên có thu nhập cao nhất")
    elif chon == "0":
        print(">>> Thoát chương trình")
    else:
        print(">>> Lựa chọn không hợp lệ")