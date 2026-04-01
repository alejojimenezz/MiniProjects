# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///

import turtle

wn = turtle.Screen()
wn.title("Arrow Key Controlled Turtle")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0) 

player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
speed = 15

def go_up():
    player.forward(speed)

def go_down():
    player.backward(speed)

def turn_left():
    player.left(45)

def turn_right():
    player.right(45)

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")

while True:
    wn.update()