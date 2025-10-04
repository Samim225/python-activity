from tkinter import *
import random
window = Tk()
window.title("samim 5 test snake game")
window.resizable(False, False)

GAME_WIDTH = 400
GAME_HEIGHT = 400
SPEED = 40
SPACE_SIZE = 30
BACKGROUND = "#3ad08d"
SNAKE_COLOR = "#F02847"
FOOD_COLOR = "#0193F3"
BODY_PARTS = 4
canva = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH)
score = 0
class Snake:
    def __init__(self):
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            canva.create_rectangle(
            x,y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=SNAKE_COLOR, tag = "snake")    
class Food:
    