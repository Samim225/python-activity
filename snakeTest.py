from tkinter import *
import random
window = Tk()
window.title("Snake Game")
GAME_HEGIT = 500
GAME_WIDTH = 500
SNAKE_COLOR = "#246f80"
FOOD_COLOR = "#8D90E6"
SPEED = 10
SPACE_SIZE = 50
BODY_PARTS = 4
BACKGROUND_COLOR = "#4B4647"
score = 0
canva = Canvas(window, bg=BACKGROUND_COLOR , height= GAME_HEGIT, width=GAME_WIDTH)
label = Label(window, text="Score:{}".format(score), font=("consolas", 40))
class Snake:
    def __init__(self):
        self.body = BODY_PARTS
        self.coordinate = []
        self.squares = []
        for i in range(BODY_PARTS):
            self.coordinate.append([0,0])
        for x,y in self.coordinate:
            canva.create_rectangle(
                x,y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill= SNAKE_COLOR, tag = "snake"
            )
class Food:
    def __init__(self):
        x = random.randint(0, GAME_HEGIT // SPACE_SIZE) * SPACE_SIZE
        y = random.randint(0, GAME_WIDTH // SPACE_SIZE) * SPACE_SIZE
        self.coordinate = [x,y]
        canva.create_oval(
            x,y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag = "food"
        )
label.pack()
canva.pack()
snake = Snake()
food = Food()
window.update()
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
screen = int((screen_height/2)) - int((window_height/2))
sce = int((screen_width/2)) - int((window_width/2))
window.geometry(f"{window_width}x{window_height}+{sce}+{screen}")
window.mainloop()