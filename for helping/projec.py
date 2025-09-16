class Boxer:
 def __init__(self,name,wieght, kickP, boxP, height, grade):
        self.name = name
        self.weight = wieght
        self.kickP = kickP
        self.boxP = boxP
        self.height = height
        self.grade = grade
 def info(self):
  print("the name is:" + self.name + " " + "The grade is :" + self.grade + " " + "The Wieght is :" + self.weight + " " + "The height is :" + self.height)
boxer1 = Boxer("Mike Tyson", "189kg", "200kg", "400kg", "180cm", "1st")
boxer2 = Boxer("", "189kg", "200kg", "400kg", "180cm", "1st")
boxer1.info()