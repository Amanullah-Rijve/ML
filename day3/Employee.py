class Employee:
    def __init__(self,name: str,salary:int):
        self.name = name
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        if value <0:
            print("Salary can't be negetive")
        else: self.__salary = value
    
e = Employee("Rohim",50000)
print(f" Current Salary: {e.salary}") # main salary

e.salary = 60000 # using setter to update salary
print(f"New Updated Salary: {e.salary}") # new updated salary
