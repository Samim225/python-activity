# import random

# qot = ["Stay hard", "never give up", "just do it", "It is never too late to be what you might have been.", "Ah, but a man's reach should exceed his grasp, Or what's a heaven for?"]
# x =random.choice(qot)
while True:
    """Person name samim or shayan"""
    samim = 0
    shayan = 0
    vote = input("Persone name: ")
    def sa(sam):
        global samim
        samim += sam
        print(samim)
    if vote == "samim" :
        sa(1)
        
        print(samim)
    # elif vote == "shayan" or "Shayan":
    #     shayan +=1
    #     print(shayan)
    else:
        print("enter an person name")
        bre
    # if samim == 10 and samim > shayan:
    #     print("the winner is: Samim")
    #     break
    # elif shayan == 10 and samim < shayan:
    #     print("the winner is: Shayan")
    #     break
    # else:
    #     print("nanan")
        