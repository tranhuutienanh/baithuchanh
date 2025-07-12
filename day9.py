from day8part3 import CreditCard, PayPal, CryptoWallet

def media_menu():
    payments = [
        CreditCard("Ronaldo", 1000000, "", ""),
        PayPal("Messi", 1000000, "", ""),
        CryptoWallet("Neymar", 1000000, "", "")
    ]

    while True:
        print("\nChọn dịch vụ:")
        print("1. Thêm phương thức thanh toán")
        print("2. Thanh toán")
        print("3. Xem số dư")
        print("4. Thoát")
        
        try:
            lua_chon = int(input("Nhập lựa chọn (1-4): "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 4.")
            continue

        if lua_chon == 1:
            print("Hệ thống chưa hỗ trợ các thanh toán này.")

        elif lua_chon == 2:
            print("\nChọn phương thức thanh toán:")
            print("1. Credit card")
            print("2. Paypal")
            print("3. Crypto wallet")

            loai = int(input("Nhập lựa chọn (1-3): "))
            if loai in [1, 2, 3]:
                payment = payments[loai - 1]
            if loai == 1:
                amount = int(input("Nhập số tiền muốn thanh toán: "))
                card_number = input("Nhập số thẻ: ")
                cvv = input("Nhập mã CVV: ")
                payment.card_number = card_number
                payment.cvv = cvv
                if payment.authenticate():
                    payment.pay(amount)
                else:
                    print("Xác thực thất bại.")
            elif loai == 2:
                amount = int(input("Nhập số tiền muốn thanh toán: "))
                email = input("Nhập email: ")
                password = input("Nhập mật khẩu: ")
                payment.email = email
                payment.password = password
                if payment.authenticate():
                    payment.pay(amount)
                else:
                    print("Xác thực thất bại.")
            elif loai == 3:
                amount = int(input("Nhập số tiền muốn thanh toán: "))
                key = input("Nhập private key: ")
                if payment.authenticate(key):
                    payment.pay(amount)
                else:
                    print("Xác thực thất bại.")

        elif lua_chon == 3:
            print("\nChọn ngân hàng hoặc ví muốn coi:")
            print("1. Credit card")
            print("2. Paypal")
            print("3. Crypto wallet")
            try:
                loai = int(input("Nhập lựa chọn (1-3): "))
                if loai in range(1, 4):
                    payment = payments[loai - 1]
                    payment.so_du()
                else:
                    print("Lựa chọn không hợp lệ.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        elif lua_chon == 4:
            print("Dừng thanh toán.")
            break

        else:
            print("Lựa chọn không hợp lệ.")

media_menu()
