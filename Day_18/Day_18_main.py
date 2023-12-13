from turtle import Turtle, Screen
import random
import colorgram

screen = Screen()
screen.colormode(255)
paint = Turtle()
colors = colorgram.extract('image.jpg', 13)
# print(colors)
screen.mode('world')
paint.penup()
paint.speed("fastest")
paint.goto(-400, 0)

for ii in range(7):
    for i in range(13):
        color = colors[random.randint(0, 12)]
        rgb = color.rgb
        paint.fd(50); paint.dot(20, rgb)
    y= ((ii+1) * 30)
    paint.goto(-400, y)

screen.exitonclick()