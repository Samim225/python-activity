# import time
# class Librarry:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self._avilible = True
#     # def borrow(self):
#     #     self.avilible = False
#     #     return self.avilible
#     def book_borrow(self):
#         if self._avilible:
#             self._avilible = False
#             print(f"The book: {self.title} rcived")
            
#         else:
#             print("hello world")
#     def recovery(self):
#         print("You have 10 socends to recover the book")
#         time.sleep(10)
#         self._avilible = True
#         print("The free trial finished")
#         time.sleep(2)
#         print(f"the existed book is {self.title}")
    
# b1 = Librarry("Ghoraza", "Samim")

# b1.book_borrow()
# b1.recovery()

        
























class Shape:
    def __init__(self,area):
        self.area = area
    def jam(self, result):
        re = self.area *3.14*result
        print(re)
so1 = Shape(20)
so1.jam(30)
