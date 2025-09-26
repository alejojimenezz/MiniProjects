import turtle
import math

turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(2)

# Parámetros del trébol
a = 200   # radio base
b = 50    # amplitud de la ondulación

turtle.penup()
for angle in range(0, 361):
    theta = math.radians(angle)
    r = a + b * math.cos(4 * theta)   # ecuación polar
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if angle == 0:
        turtle.goto(x, y)
        turtle.pendown()
    else:
        turtle.goto(x, y)

turtle.hideturtle()
turtle.done()