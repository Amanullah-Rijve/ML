# Encapsulation
'''
3 types of attributes
1.Public
2.private (__)
3. protected (_)
'''
class Account:
    def __init__(self,name,balance):
        self.name = name # public data anyone can access
        self._balance = balance  # protected data 
        self.__pin = "1234" # private data can't access
        
'''
now lets try to print those without using geeter and setter method
'''
acc = Account("karim",5000)

print(acc.name) # will print
print(acc._balance) # will work but its not good practice
print(acc.__pin) # error wont give data
''' error msg given--- print(acc.__pin) # error wont give data
        ^^^^^^^^^
AttributeError: 'Account' object has no attribute '__pin
'''




