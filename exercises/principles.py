class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def breathe(self):
        return f"{self.name} breathes."

class Mammal(Animal):
    def __init__(self, name, age, weight, legs):
        super().__init__(name, age, weight)
        self.legs = legs

class Dog(Mammal):
    def breathe(self):
        return f"{self.name} pants."

