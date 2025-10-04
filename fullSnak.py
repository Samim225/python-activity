from tkinter import *
import random
import time

GAME_WIDTH = 500
GAME_HEIGHT = 500

speed = 150

SPACE_SIZE = 10

BODY_PARTS = 50

SNAKE_COLOR = "#00FF00"       # bright green
FOOD_COLOR = "#FF0000"        # red
BACKGROUND_COLOR = "#000000"  # black

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                tag="snake"  # tag helps when we want to delete all at once
            )
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        # Store the food's top-left corner (grid-aligned)
        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR,
            tag="food"  # tag helps delete the old food easily
        )
class FoodV:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill="#01f315",
            tag="foodv"  # tag helps delete the old food easily
        )

def next_turn(snake, food, foodv):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE,
        fill=SNAKE_COLOR,
        tag="snake"
    )
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")

        canvas.delete("food")
        food = Food()  # local variable is fine; we pass it to the next call
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if x == foodv.coordinates[0] and y == foodv.coordinates[1]:
        global hidden_score 
        hidden_score +=1
        canvas.delete("foodv")
        foodv = FoodV()
        global speed
        speed = 190
        print(hidden_score)
    else:
        NONE
    if hidden_score == 3:
        canvas.delete("foodv")
        speed = 70
    else:
        NONE
    if check_collisions(snake):
        game_over()
    else:
        window.after(speed, next_turn, snake, food, foodv)
def change_direction(new_direction):
    global direction
    # Only allow a change if we're not reversing direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True
    # Check self-collision: head matches any other body part coordinates
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
def game_over():
    canvas.delete(ALL)

    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=('consolas', 70),
        text="GAME OVER",
        fill="red",
        tag="gameover"
    )



window = Tk()
window.title("Snake game")
window.resizable(False, False)
score = 0
hidden_score = 0
direction = 'down'
label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>',  lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>',    lambda e: change_direction('up'))
window.bind('<Down>',  lambda e: change_direction('down'))
snake = Snake()
food = Food()
foodv = FoodV()
next_turn(snake, food, foodv)
window.mainloop()