from turtle import Turtle, Screen
import random



screen = Screen()
screen.colormode(255)

kaoru_turtle = Turtle()
##turtle object

kaoru_turtle.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

kaoru_turtle.speed("fastest")
def draw_spirograph(size):
    for i in range(int(360/size)):
        kaoru_turtle.color(random_color())
        kaoru_turtle.circle(100)
        kaoru_turtle.setheading(kaoru_turtle.heading()+size)


draw_spirograph(5)
##needs screen to show



screen.exitonclick()

