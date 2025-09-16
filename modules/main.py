# # import turtle as tu
# # x = tu.Turtle
# # import turtle

# # t = turtle.Turtle()
# # t.shape("turtle")
# # t.color("red")
# # for _ in range(4):
# #     t.forward(100)  # Move forward 100 pixels
# #     t.right(40) 
# #     t.back(20)

# # turtle.done()
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")

# for _ in range(6):
#     t.forward(100)
#     t.right(60)
#     t.back(20)   # creates a little notch/spike

# turtle.done()
import turtle

t = turtle.Turtle()
# t.shape("turtle")
t.color("red")

# Draw hexagon
for _ in range(6):
    t.forward(100)
    t.back(10)
    t.right(60)


# Clear everything

t.hideturtle()

turtle.done()
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")

# # حلقه بیرونی برای کوچیک شدن
# for size in range(100, 20, -15):   # از 100 تا 20 هر بار 15 تا کمتر
#     for _ in range(6):             # کشیدن هگزاگون
#         t.forward(size)
#         t.right(60)

# t.hideturtle()
# turtle.done()