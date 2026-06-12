class Account: # parent calss
    # constructor
    def __init__(self,acc_num:int,name: str,balance:int):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance
    
    # display parent calss method
    def display_all(self):
        return f"Account {self.acc_num} of Md.{self.name} current balance {self.balance}"

# sub class extends to Account
class SavingsAccount(Account):
    def __init__(self, acc_num, name, balance,interest_rate):
        super().__init__(acc_num, name, balance) # parent calss super __init__
        self.interest_rate = interest_rate
    
    # adding interest to balance
    def add_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate/100)
        return f"Interest added. New Balance: {self.balance}"
    
    # display info by taking from parent calss using super method
    def display_all(self):
        base = super().display_all() # sub calss __init__ takes from parent class __init__
        return f"{base} and interest {self.interest_rate} %"
    
    # another sub class
class CurrentAccount(Account):
    def __init__(self, acc_num, name, balance,overdraft_limit):
        super().__init__(acc_num, name, balance)
        self.overdraft_limit = overdraft_limit # adding new variables 
    
    # withdraw mwthod
    def withdraw(self,amount):
        #withdraw logic
        if(self.balance + self.overdraft_limit < amount):
            return "Withdraw Failed"
        self.balance -= amount
        return f"Withdraw Success,new balance {self.balance}"
    
    # same as before dispaly all 
    def display_all(self):
        base = super().display_all()
        return f"{base} and limit {self.overdraft_limit}"

# object
p1 = Account(34,"Rafiq",50000)
# print/calling methods
print(p1.display_all())

# object
s1 = SavingsAccount(101,"karim", 10000,5)
# calling methods
print(s1.display_all())
print(s1.add_interest())

# object
c1 = CurrentAccount(202,"siam",5000,2000)
# calling methods
print(c1.display_all())
print(c1.withdraw(4000))
print(c1.withdraw(400000))