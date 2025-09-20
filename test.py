from tkinter import *
import random

root = Tk()
root.title("be adab")
root.geometry("400x600")
root.resizable(False, False)
GAME_WIDTH = 400
GAME_HEIGHT = 600
SNAKE_COKOR = "#26B0A0"
BACKGROUND = "#000000"
SPACE_SIZE = 40
SPEED = 50
BODY_SIZE = 4
FOOD_COKOR = "#E60000"
score = 0

class Snake:
    def __init__(self):
        self.body = BODY_SIZE
        self.coordinate = []
        self.squares = []
        for i in range(BODY_SIZE):
            self.coordinate.append([0,0])
        for x,y in self.coordinate:
            canva.create_rectangle(
                x,y,  x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COKOR, tag = "snake"
            )
            
class Food:
    def __init__(self):
        self.cordinate = []
        x = random.randint(0, GAME_WIDTH // SPACE_SIZE -1) * SPACE_SIZE
        y = random.randint(0, GAME_HEIGHT// SPACE_SIZE -1) * SPACE_SIZE
        self.cordinate= [x,y]
        canva.create_oval(
            x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COKOR ,tag="food"
        )
        

label=Label(root, text="Score:{}".format(score), font=("consolas", 49))
label.pack()
canva = Canvas(root, background=BACKGROUND, width=GAME_WIDTH, height=GAME_HEIGHT)
canva.pack()
snake = Snake()
food  = Food()

root.mainloop()