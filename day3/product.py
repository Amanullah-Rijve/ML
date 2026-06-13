class Product:
    def __init__(self,name:str,price:int):
        self.name = name
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value <0:
            print("negetive amount")
        else: self.__price = value
    
    def apply_discount(self,percent):
        if 0<= percent <=100:
            discount_amount = self.__price * percent /100
            self.price = self.__price - discount_amount
            return f"Discount applied. New price: {self.price}"
        else: print("Invalid discount percentage")
    
p1 = Product("SSD",5000)
print(p1.price)
p1.price = 6000
print(p1.price)
print(p1.apply_discount(99))
print(p1.apply_discount(150))

