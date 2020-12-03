class Dog:
    

    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy
    
    def bark(self):
        if self.energy < 5:
            return f"{self.name} gently boofs!"
        else:
            return f"{self.name} barks heartily"

    def __repr__(self):
        return f'''
                Name: {self.name}
                Breed: {self.breed}
                Energy: {self.energy}
            '''

my_dog = Dog("chewie", "Ekuke", 6)

print(my_dog.bark())