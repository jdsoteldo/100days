from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 480, height = 400)
start_race = False
colors = ["red", "yellow", "orange", "green", "blue", "purple", "dark slate blue"]
y_pos = [-150, -100, -50, 0, 50, 100, 150]
turtles = []

for i in range(0, 7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -220, y = y_pos[i])
    turtles.append(new_turtle)

user_choice = screen.textinput(title = "Place your bet", prompt= "Select the color of the turtle")

while user_choice.lower() not in colors:
    user_choice = screen.textinput(title = "Place your bet", prompt= "Select the color of the turtle")

if user_choice.lower() in colors:
    start_race = True
    print(f"You picked: {user_choice}")

while start_race:

    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 220:
            winner = turtle.pencolor()
            start_race = False
            if winner == user_choice:
                print(f"You've won")
            else:
                print(f"You lost. the winner is: {winner}")

screen.exitonclick()
