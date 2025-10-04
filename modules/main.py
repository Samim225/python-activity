class Person:
    def __init__(self, name, fname, sub, schName):
        self.name = name
        self.fname = fname
        self.sub = sub
        self.schName = schName
    def intro(self):
        print(f"my name is {self.name} and my father name is {self.fname}")
class Stu(Person):
    def study(self):
        print(f"I study {self.sub} in {self.schName}")

st1 = Stu("Shayan", "Samim", "Computer sneince", "Atayee")
st1.intro()
st1.study()
        