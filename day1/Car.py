class Car:
    # car clas varibale is wheels
    wheels = 4 
    
    #constructor
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        # printing info by using display method
    def display(self):
        return f"{self.year} {self.brand} {self.model} has {Car.wheels}"
    
    # create object 
car1 = Car("Toyota","Corolla",2022)
car2 = Car("Honda","Civic",2023)

# Printing info
print(car1.display())
print(car2.display())
    