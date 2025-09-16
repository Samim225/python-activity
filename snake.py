from tkinter import *
import random
window = Tk()
window.title("samim game best develaoper in the world hahha")
window.resizable(False, False)
GAME_WIDTH = 700
GAME_HIEGHT = 700
SPEED = 20
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#39F900"
FOOD_COLOR = "#FFF133"
BACKGROUND = "#31BDF4"
#adddesd



class Snake:
    pass
class Food:
    pass
    def __init__(self):
        x = random.randint(0, GAME_WIDTH // SPACE_SIZE -1) * SPACE_SIZE
        y = random.randint(0, GAME_HIEGHT // SPACE_SIZE -1) * SPACE_SIZE
        self.coordin = [y,x]
        canva.create_oval(
            x,y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill = FOOD_COLOR, tag ="food"
        )

def next_turn():
    pass
def change_dierect():
    pass
def check_collisions():
    pass
def game_over():
    pass

score = 0
label = Label(window, text="Score {}".format(score), font=("consolas",40))
label.pack()

canva = Canvas(window, bg=BACKGROUND, width=GAME_WIDTH , height=GAME_HIEGHT)
canva.pack()
snake = Snake()
food = Food()
# window.update()
# window_height = window.winfo_height()
# window_width = window.winfo_width()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

window.mainloop()