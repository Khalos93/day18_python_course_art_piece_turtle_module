import random
import turtle
from turtle import Turtle, Screen
from util import draw_modern_painting
import colorgram

turtle.colormode(255)
colors = []
extract_colors = colorgram.extract('damien_hirst_dot_painting.jpg', 10)
for color in extract_colors:
    new_color = (color.rgb[0], color.rgb[1], color.rgb[2])
    colors.append(new_color)

timmy_the_turtle = Turtle()


timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('magenta')
timmy_the_turtle.speed(10)
timmy_the_turtle.penup()

y_position = -250
x_position = -250


draw_modern_painting(timmy_the_turtle, x_position, y_position, 10, colors)


screen = Screen()
screen.exitonclick()
