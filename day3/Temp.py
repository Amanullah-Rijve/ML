class Temperature:
    def __init__(self,c):
        self.__c = c
        
        # getter
    @property
    def c(self):
        return self.__c
    
    #setter
    @c.setter
    def c(self,value):
        if value<-273.15:
            print("Temperature below absolute zero!")
        self.__c = value
    
    @property
    def f(self):  # computed property , not setter
        return (self.__c * 9/5)+32
    
    # obj and call
t = Temperature(30)
print(t.c)
print(t.f)
t.c= -300