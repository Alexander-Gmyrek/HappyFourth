import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fourth of July Fireworks")

# Create a turtle for the fireworks
firework = turtle.Turtle()
firework.speed(10)
firework.hideturtle()

# Function to draw a firework burst
def draw_firework(x, y):
    colors = ["red",  "blue", "white"]
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    for _ in range(4):
        firework.color(random.choice(colors))
        firework.forward(50)
        firework.right(170)
        firework.forward(50)
        firework.left(80)
    firework.penup()  # Lift the pen after drawing
    firework.hideturtle()

# Function to create random fireworks
def create_fireworks():
    screen.tracer(0)
    screen.clear()
    screen.bgcolor("black")
    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_firework(x, y)
    screen.update()
    screen.ontimer(create_fireworks, 1000)  # Set a longer timer for better visibility

# Start the fireworks
create_fireworks()
screen.mainloop()
