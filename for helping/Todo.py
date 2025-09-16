class ToDo:
    def __init__(self):
        self.do = []
    def adding(self, work):
        self.do.append(work)
    def show(self):
     for work in self.do:
        print(work)
    def remove(self, work):
       if work in self.do:
          self.do.remove(work)
task = ToDo()
task.adding("go to football clock 4")
task.adding("shafe is go")
task.adding("shafe is dog")
task.remove("shafe is go")
task.show()