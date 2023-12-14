import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Emter a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.shapesize()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        if racer.xcor() > 239:
            winning_color = racer.pencolor()
            if winning_color == user_bet:
               turtle.write(f"You won! The {winning_color} turtle is the winner")
            else:
                turtle.write(f"You Lost. The {winning_color} turtle is the winner")
            is_race_on = False
        else:
            distance = random.randint(0,10)
            racer.forward(distance)




screen.exitonclick()
