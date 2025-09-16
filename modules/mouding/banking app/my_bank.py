balance = 0
def deposit(bala):
    global balance
    balance += bala
    print(balance)

deposit(500)

def withdraw(bala):
    global balance
    if bala <= balance:
        balance -= bala
        print(balance)

    else:
        print("poor man no money is in your balance")
# withdraw(5000)

