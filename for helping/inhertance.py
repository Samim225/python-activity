class Viechle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def going(self):
        print("it is moving")
    
class Car(Viechle):
    def speed(self):
        print(f"{self.name} speed is to much my brother and the color is {self.color}")
class Bike(Viechle):
    def saying(self):
        print(f"This is {self.name} that it's color is {self.color}")
    def going(self, breed):
        self.breed = breed
        print("IHEHE")
        super().going()
        




car = Car("Lambar gambar", "RED BLOODY")
car.going()
car.speed()
bike = Bike("T_2012", "GREEN GREATY")
bike.saying()
bike.going()

