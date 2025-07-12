from abc import ABC,  abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def authenticate(self):
        return False

    @abstractmethod
    def pay(self, amount):
        pass
    
    def check_balance(self):
        print(f"Số dư còn {self.balance}")


class CreditCard(PaymentMethod):
    def __init__(self, user_name, balance, card_number, cvv):
        self.balance = balance
        self.user_name = user_name
        self.card_number = card_number
        self.cvv = cvv

    def authenticate(self):
        if self.card_number.isdigit() and 8 <= len(self.card_number) < 12 and self.cvv.isdigit() and 8 <= len(self.cvv) < 12:
            print("Thẻ đã được uỷ quyền")
            return True
        else:
            print("Thẻ chưa được uỷ quyền")
            return False
        
    def pay(self, amount):
        if amount > self.balance:
            print("Số dư ko đủ")
        else:
            self.balance -= amount
        print(f"Đã trả {amount} đồng")
    
    def check_balance(self):
        print(f"Số dư còn {self.balance}")
    
    def so_du(self):
        print(f"Số dư còn {self.balance} đồng")
    

class PayPal(PaymentMethod):

    def __init__(self, user_name, balance, email, password):
        self.balance = balance
        self.user_name = user_name
        self.email = email
        self.password = password

    def authenticate(self):
        if "@" in self.email and self.password.isdigit() and 8 <= len(self.password) < 12:
            print("Email và password hợp lệ")
            return True
        else:
            print("Lỗi")
            return False

    def pay(self, amount):
        if amount > self.balance:
            print("Số dư ko đủ")
        else:
            self.balance -= amount
            print(f"Đã trả {amount} đồng")
    
    def so_du(self):
        print(f"Số dư còn {self.balance} đồng")


class CryptoWallet(PaymentMethod):
    def __init__(self, user_name, balance, wallet_address, private_key):
        self.balance = balance
        self.user_name = user_name
        self._wallet_address = wallet_address
        self.__private_key = private_key

    def authenticate(self, private_key_new):
        if self.__private_key == private_key_new:
            print("Ví đã được uỷ quyền")
            return True
        else:
            print("Uỷ quyền thất bại")
            return False

    def pay(self, amount):
        if amount > self.balance:
            print("Số dư ko đủ")
        else:
            self.balance -= amount
        print(f"Đã bán {amount} coin")
    
    def so_du(self):
        print(f"Số dư còn {self.balance} đồng")












