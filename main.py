from turtle import Turtle, Screen
import random

"""import colorgram
colors = colorgram.extract('artoncontemporary-damien-hirst-damien-hirst-the-complete-spot-paintings-1986-2011.jpg', 20)

rgb_colors = []

for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)"""

screen = Screen()
screen.colormode(255)
color_list=[(225, 223, 209), (0, 0, 0), (165, 87, 38), (111, 35, 63), (2, 113, 179), (221, 176, 8), (2, 97, 80), (172, 163, 127), (200, 75, 118), (189, 54, 97), (79, 35, 70), (176, 201, 198), (196, 215, 210), (222, 216, 153), (80, 128, 48), (6, 104, 106), (188, 210, 215), (212, 185, 180), (176, 199, 202), (204, 94, 57)]

k= Turtle()
k.shape("turtle")
k.color("white")
k.speed("fastest")


"""k.penup()
k.right(180)
k.forward(370)
k.right(180)
k.right(90)
k.forward(370)
k.left(90)"""

k.penup()
k.hideturtle()
k.goto(-360, -360)


def line_dot():
    for i in range(10):
        k.dot(20,random.choice(color_list))
        k.penup()
        k.forward(50)

def cross_left():
    k.right(270)
    k.forward(50)
    k.left(90)
    k.forward(50)

def cross_right():
    k.right(90)
    k.forward(50)
    k.right(90)
    k.forward(50)

for i in range(5):
    line_dot()
    cross_left()
    line_dot()
    cross_right()







screen.exitonclick()





