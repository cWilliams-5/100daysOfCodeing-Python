from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_back():
    tim.back(10)

def turn_left():
    tim.left(45)

def turn_right():
    tim.right(45)

screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_back)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.exitonclick()