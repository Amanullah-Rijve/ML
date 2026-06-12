class Employee: # parent class
    # constructor
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    # parent clas into printing method
    def details(self):
        return f"{self.name} erans {self.salary}"

# child class
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary) # child class super class
        self.team_size = team_size
        
        # child class info printing
    def details(self):
        base= super().details() # calling parent class 
        return f"{base} and managesr {self.team_size} people"

# object
e = Employee("karim",30000)
m = Manager("Rijve",80000,5)

# print all
print(e.details())
print(m.details())