# inheritance & polymorphism
class Animal:
    def __init__(self,name):
        self.name = name
        #parent class
    def speak(self):
        return f"{self.name} makes a sound"

#child calss
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
    #child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# object variable
d = Dog("Leo")
c = Cat("Doraemon")

# printing value
print(d.speak())
print(c.speak())

'''
here Animal is the supper class , jekhane child calss Dog and Cat
Animal er power (method-speak()) eta use/override krte partece,
etai inhertance
and eta ke polymorphism o bola jay same method bbut different 
behaviour,
'''
