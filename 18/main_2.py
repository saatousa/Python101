import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()

# 18-0
tim.shape("classic")
# tim.color("LightPink2")


# 18-1
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# 18-2
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# 18-3
# colors = ["hot pink", "light pink", "orange", "khaki", "thistle", "dark gray", "rosy brown", "powder blue"]
#
#
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
#

# 18-4
# # For this you need the turtle module not the object.
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple


# angles = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.pensize(15)
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(angles))
#     tim.forward(25)


# 18-5
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# tim.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         # heading() returns the current turtle heading
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)

# This has to happened after everything we've done with the turtle
screen = Screen()
screen.exitonclick()
