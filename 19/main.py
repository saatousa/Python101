import turtle
from turtle import Turtle, Screen


import random
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "green", "orange", "yellow", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        # if we 250-(40/2) = 230. turtle is 40*40 and coordinate for the end of the window is 250
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
