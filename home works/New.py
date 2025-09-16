# class animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def move(self):
#         print("Move")
    
# class bard(animal):
#     pass     
# class fish (animal):
#         pass    



# animal1 = animal("animal",23)
# bard1 = bard("bard",623)
# fish1= fish("fish",223)
# for Y in (animal1,bard1,fish1):
#     print(Y.name)





class number:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        x = self.num
        self.num += 1
        return x
loop = number()
theiter = iter(loop)
print(next(theiter))
print(next(theiter))

#torrent توشه
        