from tkinter import *
import random 
root = Tk()
root.resizable(False, False)
GAME_HEIGHT = 500
GAME_WIDTH = 500
SPACE_SIZE = 50
BODY_PARTS = 4
SNAKE_COLOR = "#a01244"
FOOD_COLOR = "#000000"
SPEED = 20
score = 0
BACKGROUND = "#a22222"
canva = Canvas(root, bg=BACKGROUND, width = GAME_WIDTH, height = GAME_HEIGHT)
label = Label(root, text="Score {}".format(score), font=("consolas", 40))
label.pack()
class Snake:
	def __init__(self):
		self.body = BODY_PARTS
		self.coor = []
		self.squares = []
		for i in range(BODY_PARTS):
			self.coor.append([0,0])
		for x,y in self.coor:
			canva.create_rectangle(
				x,y, x+ SPACE_SIZE, y + SPACE_SIZE,
				fill = SNAKE_COLOR, tag = "snake")
class Food:
	def __init__(self):
		x = random.randint(0, GAME_HEIGHT // SPACE_SIZE -1) * SPACE_SIZE
		y = random.randint(0, GAME_WIDTH // SPACE_SIZE -1) * SPACE_SIZE
		self.coor = [x,y]
		canva.create_oval(
			x,y, x + SPACE_SIZE, y + SPACE_SIZE,
			fill = FOOD_COLOR , tag = "food")
snake = Snake()
food = Food()
canva.pack()
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
windows_x = int((screen_width/2) - (window_width/2))
windows_y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{windows_x}+{windows_y}")


root.mainloop()