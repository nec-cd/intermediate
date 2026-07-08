from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

finish_line= Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(230, -200)
finish_line.right(270)
finish_line.pendown()
finish_line.pensize(20)
finish_line.pencolor("black")
finish_line.forward(400)



fighter=screen.textinput(title="Choose your fighter", prompt= "Who's your gladiator? Pick a color:")
print(fighter)

colors= ["pink", "orange", "yellow", "green", "blue", "purple"]
starting_y=[-70, -40, -10, 20, 50, 80]

all_turtles=[]

#k.goto(-230, -100)
for turtle_index in range(0, 6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y[turtle_index])
    all_turtles.append(new_turtle)

if fighter:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle=turtle.pencolor()
            if winning_turtle==fighter.lower():
                print(f"You win! The {winning_turtle} turtle wins!")
            else:
                print(f"You lost! The {winning_turtle} turtle wins!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()