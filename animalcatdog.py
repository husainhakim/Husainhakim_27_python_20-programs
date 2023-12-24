
        #Create a base class called “Animal” and two subclasses, “Dog” and “Cat.” Add
#methods and attributes specific to each subclass.

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"The {self.species} says {self.sound}"

class Dog(Animal):
    def __init__(self, breed, size):
        super().__init__("Dog", "Woof!")
        self.breed = breed
        self.size = size

    def dog_info(self):
        return f"This is a {self.size} {self.breed} dog."

class Cat(Animal):
    def __init__(self, hicolor, baby):
        super().__init__("Cat", "Meow!")
        self.furcolor = hicolor
        self.baby = baby

    def cat_info(self):
        return f"This {self.species} has {self.furcolor} fur and loves playing with {self.baby}."

mydog = Dog("Golden Retriever", "baby")
mycat = Cat("Orange", "baby")


print(mydog.make_sound())  
print(mydog.dog_info())    

print(mycat.make_sound())  
print(mycat.cat_info())    