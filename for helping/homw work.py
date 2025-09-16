class Viechle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

class Lam(Viechle):
    def __init__(self, name, brand, speed):
        super().__init__(name, brand)
        self.speed = speed

    def showInfo(self):
        print(f"The brand is: {self.brand} and the name is: {self.name} And The speed is: {self.speed}")
c1 = Lam("Super Car", "Lamborghini", "230km")

class T210(Lam):
    def info(self):
        print(f"NEW MODEL IS : {self.name}")

c2 = T210("T-2025", "LAMBORGHINI", "302km")
c2.info()
c1.showInfo()




