class Animal:
    def __init__(self, name, age, spic):
        self.spic = spic
        self.name = name
        self.age = age
    def make_sound(self):
        print(f"The {self.name} some animal generic sound")
    def to_string(self):
        print(f"Name- {self.name} age- {self.age}")
    
class Loin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age,"Loin")

    def sound(self):
        print(f"The {self.name} is: Roar!")
    
class Parrot(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Parrot")
    def sound_making(self):
        print("Squawk")
    def speak(self):
        print(f"{self.name} says: hello wat is yr name") 
class Snake(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Snake")
    def sound_making(self):
        print("Hisss")
class Zoo:
    def __init__(self):
        self.animal = []
    def add_animal(self)
        if not isinstance(self.animal, Animal):
            print("Only animals allowed")
             
        else:
            self.animal.append(Animal)

loin = Loin("Simba", 5)
parrot = Parrot("Polly", 2)
snake = Snake("kaa", 4)
zoo = Zoo()
# zoo.add_animal("loin")
zoo.add_animal("parrot")
# zoo.add_animal("snake")
parrot.speak()    