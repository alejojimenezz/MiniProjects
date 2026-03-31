# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///

import turtle

# 1. Setup the screen
wn = turtle.Screen()
wn.title("Arrow Key Controlled Turtle")
wn.bgcolor("white")
wn.setup(width=600, height=600)
# Turn off automatic screen updates for manual control
wn.tracer(0) 

# 2. Create the turtle
player = turtle.Turtle()
player.shape("turtle") # The default shape can also be an "arrow"
player.color("red")
player.penup() # Lifts the pen so it doesn't draw lines when moving
speed = 15 # Movement speed

# 3. Define the movement functions
def go_up():
    """Moves the turtle forward in its current direction."""
    player.forward(speed)

def go_down():
    """Moves the turtle backward in its current direction."""
    player.backward(speed)

def turn_left():
    """Turns the turtle left by a set angle."""
    player.left(45) # Turn angle can be adjusted

def turn_right():
    """Turns the turtle right by a set angle."""
    player.right(45) # Turn angle can be adjusted

# Alternative movement (absolute headings, not relative turning):
# def go_north():
#     player.setheading(90)
#     player.forward(speed)
# ...and so on

# 4. Bind the key presses to the functions
wn.listen() # Tells the program to listen for keyboard input
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")

# 5. Main game loop (necessary for continuous responsiveness)
while True:
    wn.update() # Manually updates the screen since tracer is off
    # Add other game logic here if needed (e.g., collision checks)