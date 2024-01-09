import turtle as turtle_module
import random

turtle_module.colormode(255)
t = turtle_module
color_list = [(188, 19, 46), (244, 233, 64), (217, 239, 245), (195, 76, 34), (218, 66, 106), (13, 143, 89),
              (18, 125, 173), (196, 176, 17), (108, 182, 209), (208, 154, 91), (238, 232, 3),
              (25, 40, 75), (36, 43, 111), (78, 175, 96), (181, 44, 65), (217, 67, 47), (217, 129, 153),
              (125, 185, 120), (238, 161, 180), (7, 61, 38), (147, 209, 220), (8, 91, 52), (5, 86, 109), (160, 30, 27),
              (237, 170, 163), (158, 211, 188)]

t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.speed("fastest")
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
