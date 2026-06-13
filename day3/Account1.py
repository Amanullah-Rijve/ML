#  encapsulation method
class Account: 
    # constructor
    def __init__(self,acc_num:int,name: str,balance:int):
        self.acc_num = acc_num
        self.name = name
        self.__balance = balance # private
    
    @property # getter
    def balance(self):
        return self.__balance
    
    @balance.setter # setter
    def balance(self,value):
        if value <0:
            print("Balance can't be negetive")
        else: self.__balance = value
    
    # private method
    def __validate_pin(self,pin):
        if pin=="1234":
            return True
        else: return False
    
    def withdraw(self,amount,pin):
        if not self.__validate_pin(pin):
            print("Wrong pin")
            return
        if amount > self.__balance:
            print("Insufficient balance")
        else: 
            self.__balance -=amount
        print(f"Withdraw successful. New balance: {self.__balance}")

acc = Account(101, "Karim", 5000)

print(acc.balance)        # 5000
acc.balance = -100        # rejected
print(acc.balance)        # still 5000

acc.withdraw(1000, "1234")  # success, balance = 4000
acc.withdraw(500, "0000")   # Wrong PIN
acc.withdraw(10000, "1234") # Insufficient balance