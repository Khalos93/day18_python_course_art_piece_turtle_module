from turtle import Turtle, Screen
from matplotlib import colors
import random


timmy_the_turtle = Turtle()

colors = list(colors.CSS4_COLORS.keys())

timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('magenta')
timmy_the_turtle.speed(10)
timmy_the_turtle.penup()

y_position = -250
x_position = -250


for _ in range(0, 10):
    y_position += 50
    timmy_the_turtle.setx(x_position)
    timmy_the_turtle.sety(y_position)
    for _ in range(0, 10):
        timmy_the_turtle.dot(20, 'red')
        timmy_the_turtle.forward(50)


screen = Screen()
screen.exitonclick()