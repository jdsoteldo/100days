import turtle
import random

timmy = turtle.Turtle()
timmy.color("red")
timmy.shape("turtle")


# draw a square
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)


# draw a dotted line
# for _ in range(20):
#     timmy.forward(30)
#     timmy.penup()
#     timmy.forward(30)
#     timmy.pendown()

colors = ['blue', 'green yellow', 'pale goldenrod', 'dark green', 'cyan', 'green', 'dark khaki', 'olive drab']

def draw(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for x in range(3, 11):
    draw(x)
    timmy.color(random.choice(colors))
