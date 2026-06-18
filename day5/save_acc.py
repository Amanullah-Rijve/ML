import json
import os

# save data
def save_account(account_data,filename): # 2 ta variables declare krci parameter e
    with open(filename,"w") as f: # file write krbo
        json.dump(account_data,f,indent=4) # dump korbe account data 
    print(f"Account saved to {filename}") # file name print
    
# load account data
def load_account(filename):
    if not os.path.exists(filename):
        return "file dosen't exsist"
    with open(filename,"r") as f:
        return json.load(f)
    
# test data - in json file formate
aacount = {
    "acc_num":101,
    "name": "karim",
    "balance": 5000
}

# output test
save_account(aacount,"account.json")
loaded = load_account("account.json")
print(loaded)