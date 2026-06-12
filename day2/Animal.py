class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")
        self.species = "Dog"


d = Dog("Rex")
print(d.species)
print(d.speak())