# custome balance checking error
class BalanceError(Exception):
    def __init__(self,message):
        super().__init__(message) 

# custom pin check error
class InvalidPinError(Exception):
    def __init__(self,message):
        super().__init__( message)

# account calss
class Account:
    def __init__(self,acc_num:int,name:str,balance:int):
        self.acc_num = acc_num
        self.name= name
        self.__balance = balance # private
    
    # getter method / decorator
    @property
    def balance(self):
        return self.__balance
    
    # pin validation private method
    def __validPin__(self,pin):
        return pin == "1234"
    
    # withdraw
    def withdraw(self,amount,pin):
        if not self.__validPin__(pin): # if valid pin method fails
            raise InvalidPinError("Wrong pin")
        if amount > self.__balance: # if balance is less
            raise BalanceError("Not Enought balance")
        self.__balance -=amount # update balance
        print(f"Withdraw succesful . New balance: {self.__balance}")
        

acc  = Account(101,"Rafiq",50000)

#test case 1
try: 
    acc.withdraw(1000,"1234") # success
except InvalidPinError as e:
    print(f"Pin incorrect: {e}")
except BalanceError as e:
    print(f"Balance error: {e}")
finally:
    print("Transaction complete")

#test case 2 wrong pin
try:
    acc.withdraw(30000,"0000")
except InvalidPinError as e:
    print(f"Pin Error : {e}")
except BalanceError as e:
    print(f"Balance error; {e}")
finally:
    print("Transaction complete")

# test case 3 not enought balance
try:
    acc.withdraw(1000000000,"1234")
except BalanceError as e:
    print(f"Balance error: {e}")
except InvalidPinError as e:
    print(f"Pin Error: {e}")
finally:
    print("Transcation completed")