import turtle
import math
from matplotlib import pyplot as plt

turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(2)

# Parámetros del trébol
a = 150   # radio base
b = 30    # amplitud de la ondulación
f = 1.2   # factor de escala
n = 4     # numero de petalos
deg = 25

while deg >= -45 and deg <= 45:
    gamma = math.radians(deg) # rotacion
    break
else:
    print("La rotacion debe estar entre -45 y 45 grados")
    gamma = math.radians(0)


gammaPos = math.pi/4    # angulo maximo
gammaNeg = -math.pi/4   # angulo minimo

turtle.penup()
for angle in range(0, 361):
    theta = math.radians(angle)
    r = a + b * math.cos(n * theta)   # ecuación polar
    x = f * r * math.cos(theta + gamma)
    y = f * r * math.sin(theta + gamma)
    if angle == 0:
        turtle.goto(x, y)
        turtle.pendown()
    else:
        turtle.goto(x, y)

turtle.hideturtle()
turtle.done()

#TODO: Matplotlib window changing parameters