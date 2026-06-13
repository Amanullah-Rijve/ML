# now lets use the getter and setter
# use @property decorator
class Account:
    def __init__(self,name,balance):
        self.name = name # public data 
        self.__balance = balance # private data
    
    @property  # getter
    def balance(self):
        return self.__balance
    
    @balance.setter # setter
    def balance(self,value):
        if value <0:
            print("Balance can't be negetive")
        else: self.__balance = value
        
acc = Account("Rahhim",5000)
print(acc.balance) # gettert call - 
acc.balance =7000 # setter call
print(acc.balance) # 7000 new balance
acc.balance = -100 # negetive amount
'''
output:
5000
7000
Balance can't be negetive
'''
