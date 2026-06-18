import json

# dictionary = JSON file save
data ={
    "name":"karim",
    "balance": 5000,
    "transaction": [1000,2000,3000]
}

with open("account.json","w") as f:
    json.dump(data,f,indent=4) # formating indent=4

# json file load to dictonary
with open ("account.json","r") as f:
    loaded = json.load(f)
    print(loaded["name"])
    print(loaded["balance"])
