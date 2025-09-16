class BankAcc:
    def __init__(self, owner, blance):
        self.owner = owner
        self.blance = blance

    def deposit(self, ammount):
     self.blance += ammount
    def withdraw(self, ammount):
      if self.blance >= ammount:
       self.blance -= ammount
      else:
       print("You have no blance Man")
    def showpro(self):
     print(f"The blance is {self.blance}")
owner = BankAcc("Samim" , 90)
owner.withdraw(50)
owner.deposit(120)
owner.showpro()
