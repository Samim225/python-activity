# from abc import ABC, abstractmethod
# class Animal:
#     def __init__(self, name):
#         self._name = name
#     @abstractmethod
#     def sound(self):
#         pass
# class dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#     def sound(self):
#         print(f"The {self._name} says WOOF! WOOF!")
#         return super().sound()
# class cat(Animal):
#      def sound(self):
#         print(f"The {self._name} says MEOW! MEWO!")
#         return super().sound()
# a1 = Animal("")
# d1 = dog("Alex")
# c1 = cat("Sandra")

# d1.sound()
# c1.sound()


from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self):
     @abstractmethod
     def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "WOOF woof"
class cat(Animal):
     def sound(self):
        return "MEOW meow"
anim = [dog(), cat()]
for animal in anim:
    print(f"{animal.__class__.__name__} says: {animal.sound()}")