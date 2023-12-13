from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSlateGrey", "DarkOliveGreen4")

##make a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

##make a dashed line

# for _ in range(10):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

## make a triangle,square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

# sides = [3, 4, 5, 6, 7, 8, 9, 10]
# screen = Screen()
# screen.colormode(255)
# for i in sides:
#     turn = 360 / i
#     red = random.randint(1, 255)
#     blue = random.randint(1, 255)
#     green = random.randint(1, 255)
#     timmy.pencolor(red,green,blue)
#     s = 0
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(turn)
#         s += 1
# screen.exitonclick()

## make the turtle do a random walk with thicker lines and the same color change

# screen = Screen()
# screen.colormode(255)
# timmy.pensize(10)
# for _ in range(100):
#     red = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     green = random.randint(0, 255)
#     timmy.pencolor(red,green,blue)
#     direction = (random.randint(0,3) * 90)
#     timmy.setheading(direction)
#     timmy.forward(10)

#draw a spirograph
screen = Screen()
screen.colormode(255)
timmy.pensize(1)
timmy.speed("fastest")
direction = 360
for i in range(50):
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    timmy.pencolor(red,green,blue)
    timmy.setheading(direction)
    timmy.circle(50)
    direction += -(360/50)

screen.exitonclick()