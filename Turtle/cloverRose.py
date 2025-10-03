import turtle
import math

turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(3)

# Parámetros del trébol
a = 100   # radio base
b = 25    # amplitud de la ondulación
f = 1.2     # factor de escala
gamma = 0 # rotacion
gammaPos = math.pi/4    # angulo maximo
gammaNeg = -math.pi/4   # angulo minimo

turtle.penup()
for angle in range(0, 361):
    theta = math.radians(angle)
    r = a * math.cos(4 * theta)   # ecuación polar
    x = f * r * math.cos(theta + gamma)
    y = f * r * math.sin(theta + gamma)
    if angle == 0:
        turtle.goto(x, y)
        turtle.pendown()
    else:
        turtle.goto(x, y)

turtle.hideturtle()
turtle.done()