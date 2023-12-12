from turtle import Turtle, Screen
#https://docs.python.org/3/library/turtle.html

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkSlateGrey", "DarkOliveGreen4")

my_screem = Screen()
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
my_screem.exitonclick()