x = input("file name:")

try:
    with open(x, 'r') as file:
        print(file.read())
    say = input("you want to add something")
    if say == "yes" or "Yes":
        s = input("say what you want: ")
        with open(x, 'a') as file:
            file.write(s)
        with open(x, 'r') as file:
            print(file.read())
    # elif say == "create" or "Create":
    #      s = input("file name: ")
    #      with open(x, 'x') as file:
    #         file.write(s)

    
except:
    print("no file in directory")

finally:
    print("program finished")


