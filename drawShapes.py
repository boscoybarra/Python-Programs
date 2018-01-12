import turtle

# Function to draw squares
def draw_square(someone):
    for i in range(1, 5):
        someone.forward(100)
        someone.right(90)

# Function to draw trianles
def draw_triangle(someone):
    for idea in range(1, 4):
        someone.forward(100)
        someone.left(120)

# Function to draw art!
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    # All about Brad Square Lover
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    # All about Angie Circle Lover

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    # All about Pat Triangle Lover

    pat = turtle.Turtle()
    pat.shape("turtle")
    pat.color("green")
    draw_triangle(pat)

    window.exitonclick()

draw_art()
