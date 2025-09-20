# x = input("+ - / *:")
# y = input("The value :")
# i = input("socend Value:")
# def a():
#  if x == "+":
#   result = int(i) + int(y)
#   print(f"The result is {result}")
#  elif x == "-":
#   result = int(i) - int(y)
#   print(f"The result is {result}")

#  elif x == "/":
#   result = int(i) / int(y)
#   print(f"The result is {result}")

#  elif x == "*":
#   result = int(i) * int(y)
#   print(f"The result is {result}")

#  else:
#   print("enter the vale")
vote = input("Enter name:")
sa = 0
sa2 = 0
while True :
        if vote == "samim":
            sa +=1
            print(sa)
            vote = input("enter name: ")
            if sa == 10:
                   print("Samim is Winner and father of Shayan")
                   break
            else:
                True
        elif vote == "shayan":
                sa2 +=1
                print(sa2)
                vote = input("enter name: ")
                if sa == 10:
                   print("Shayan is Winner and father of Samim")
                   break
                else:
                    True
        else:
              print("enter name")   