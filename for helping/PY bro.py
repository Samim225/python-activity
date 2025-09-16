# class Grade:
#     def __init__(self, name, grad):
#         self.name = name
#         self.grad = grad
#     def check(self):
#         if self.grad >= 10:
#             print("You are passed")
#         else:
#             print("You are not passed")
#     def PON(self):
#         print(f"The name: {self.name} The result: {self.grad}")
# student = Grade("Samim", 20)
# student2 = Grade("Ahmad", 9)
# student.check()
# student.PON()
# student2.check()
# student2.PON()
class Grade:
    def __init__(self, name, grad):
        self.name = name
        self.grad = grad
        # self.list = list
    def PON(self):
        # print(self.grad)
        
        result = sum(self.grad)
        # result2 = result / 5
        # jam = self.grad + am
        print(f"The name: {self.name} The result: {result}")
    # def check(self):
    #   if self.grad >= 140:
    #          print("You are passed")
    #   else:
    #          print("You are not passed")

student = Grade("Samim", [20, 40, 30, 32, 23, 10])
student.PON()
# student.check()