x = input("+ - / *:")
y = input("The value :")
i = input("socend Value:")
def a():
 if x == "+":
  result = int(i) + int(y)
  print(f"The result is {result}")
 elif x == "-":
  result = int(i) - int(y)
  print(f"The result is {result}")

 elif x == "/":
  result = int(i) / int(y)
  print(f"The result is {result}")

 elif x == "*":
  result = int(i) * int(y)
  print(f"The result is {result}")

 else:
  print("enter the vale")