import json
import os

class Account:
    def __init__(self,acc_num:int,name:str,balance:int):
        self.acc_num = acc_num
        self.name = name
        self.__balance = balance # private 
    
    @property # getter
    def balance(self):
        return self.__balance
    
    def save_to_file(self):
        data = { # dynamic json file data
            "acc_num": self.acc_num,
            "name": self.name,
            "balance":self.__balance
        }
        with open(f"account_{self.acc_num}.json","w") as f:
            json.dump(data,f,indent=4)
            print(f"Account Saved : account_{self.acc_num}.json ")
            
    @classmethod
    def load_from_file(cls,acc_num):
        filename = f"account_{acc_num}.json"
        if not os.path.exists(filename):
            print("file not found")
        with open(filename,"r") as f:
            data = json.load(f)
        return cls(data["acc_num"],data["name"],data["balance"])
    
    def add_transaction(self,amount,type):
        # loading previous data
        filename = f"account_{self.acc_num}.json"
        with open(filename,"r") as f:
            data = json.load(f)
        
        # if not list than make empty list
        if "transactions" not in data:
            data["transactions"] = [] #empty list
        
        #ad new transaction
        data["transactions"].append({
            "type": type,
            "amount": amount
        })
        
        # update balance
        if type =="deposit":
            data["balance"]+=amount
            self.__balance +=amount
        elif type =="withdraw":
            data["balance"]-=amount
            self.__balance -= amount
        
        # save file
        with open(filename,"w") as f:
            json.dump(data,f,indent=4)
        print(f"{type} of {amount} recorder" )
            
acc = Account(101,"Karim",5000)
acc.save_to_file()

loaded_acc = Account.load_from_file(101)
print(loaded_acc.balance)  # 5000
print(loaded_acc.name)     # Karim

acc.add_transaction(1000, "deposit")
acc.add_transaction(500, "withdraw")

loaded = Account.load_from_file(101)
print(loaded.balance)