import colorgram
import turtle as turtle_module
import random


colors_list = [(249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70),
               (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149),
               (65, 203, 229),
               (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9),
               (248, 11, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61), (5, 38, 33), (67, 219, 155)]

turtle_module.colormode(255)
turtle = turtle_module.Turtle()


turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(colors_list))
    turtle.penup()
    turtle.forward(50)
    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = turtle_module.Screen()
screen.screensize(2000, 1500)
screen.exitonclick()
