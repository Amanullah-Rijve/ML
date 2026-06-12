class Vehicle: # parent / super class
    
    # constructor
    def __init__(self,brand,wheel):
        self.brand = brand
        self.wheel= wheel
        
    #super class method displaying info
    def desc(self):
        return f"{self.brand} has {self.wheel} wheels"
    
    #child class
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,wheel=4) # calling the inin of parent calss to use hios power
        self.model = model
    
    # child classs info desplaying
    def desc(self):
        base = super().desc() # parent class method
        return f"{base} ,model: {self.model} "

# child class
class Motorcycle(Vehicle):
    def  __init__(self,brand):
        super().__init__(brand,wheel=2)

# creating object
c=Car("Toyota","Corolla")
m = Motorcycle("Royal")

#prining all
print(c.desc())
print(m.desc())