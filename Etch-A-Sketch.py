from turtle import Turtle, Screen


k= Turtle()
screen = Screen()

def move_forward():
    k.forward(10)

def move_backward():
    k.backward(10)

def turn_clockwise():
    current_heading = k.heading()
    k.setheading(current_heading -10)

def turn_counterclockwise():
    current_heading = k.heading()
    k.setheading(current_heading +10)

def clear():
    k.clear()
    k.penup()
    k.home()
    k.pendown()

screen.listen()
screen.onkey(key= "w", fun= move_forward)
screen.onkey(key= "s", fun= move_backward)
screen.onkey(key= "a", fun= turn_counterclockwise)
screen.onkey(key= "d", fun= turn_clockwise)
screen.onkey(key= "c", fun= clear)










screen.exitonclick()