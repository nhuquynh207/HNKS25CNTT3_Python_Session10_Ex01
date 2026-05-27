# input:dữ liệu mẫu,
    # 2.mã sp (Str),tên sp (str),số lượng (int),đơn giá(int)
    # 3.mã sp(str),số lượng mới (int)
    # 4.mã sp(int)

# output:menu chúc năng
# 1.bảng giỏ hàng
# 2.thêm sp mới vào cuối danh sách,cộng dồn số lượng nếu trùng id,thông báo
# 3.cập nhật số lượng sp,thông báo
# 4.xóa sp khỏi ds,thông báo
# 5.thông báo thoát chương trình

cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n========== SHOPEE CART MANAGEMENT SYSTEM ==========")

    print("[1] Xem chi tiet gio hang & Tinh tong tien")
    print("[2] Them san pham moi / Cong don so luong")
    print("[3] Cap nhat so luong san pham")
    print("[4] Xoa san pham khoi gio hang")
    print("[5] Thoat chuong trinh")

    choice = input("\nMoi ban chon chuc nang (1-5): ").strip()
    if not choice.isdigit():
        print("Lua chon khong hop le!")
        continue

    choice = int(choice)
    if choice == 1:
        total_quantity = 0
        total_price = 0

        print("\n===== CHI TIET GIO HANG =====")
        print("STT | Ma SP | Ten San Pham | SL | Don Gia | Thanh Tien")

        for i in range(len(cart_items)):
            item = cart_items[i]

            product_id = item[0]
            product_name = item[1]
            quantity = item[2]
            price = item[3]

            subtotal = quantity * price

            total_quantity += quantity
            total_price += subtotal

            print(
                i + 1,
                "|",
                product_id,
                "|",
                product_name,
                "|",
                quantity,
                "|",
                f"{price:,}đ",
                "|",
                f"{subtotal:,}đ"
            )

        print("\nTong so luong san pham:", total_quantity)
        print("TONG TIEN THANH TOAN:", f"{total_price:,}đ")
    elif choice == 2:
        product_id = input("Nhap ma san pham: ").strip()
        product_name = input("Nhap ten san pham: ").strip()

        try:
            quantity = int(input("Nhap so luong: "))
            price = int(input("Nhap don gia: "))

            if quantity <= 0 or price < 0:
                print("So luong hoac don gia khong hop le!")
                continue

        except:
            print("Du lieu nhap khong hop le!")
            continue

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] += quantity
                found = True
                print("Da cong don so luong!")
                break

        if found == False:
            cart_items.append([product_id, product_name, quantity, price])
            print("Them san pham thanh cong!")
    elif choice == 3:
        product_id = input("Nhap ma san pham can cap nhat: ").strip()

        try:
            new_quantity = int(input("Nhap so luong moi: "))

            if new_quantity <= 0:
                print("So luong khong hop le!")
                continue
        except:
            print("Du lieu khong hop le!")
            continue
        found = False
        for item in cart_items:
            if item[0] == product_id:
                item[2] = new_quantity
                found = True
                print("Cap nhat thanh cong!")
                break

        if found == False:
            print("Ma san pham khong ton tai trong gio hang!")
    elif choice == 4:
        product_id = input("Nhap ma san pham can xoa: ").strip()

        found = False

        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)
                found = True
                print("Xoa san pham thanh cong!")
                break

        if found == False:
            print("Ma san pham khong ton tai trong gio hang!")
    elif choice == 5:
        print("Da thoat chuong trinh!")
        break
    else:
        print("Lua chon phai tu 1 den 5!")