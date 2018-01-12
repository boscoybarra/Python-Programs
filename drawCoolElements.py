import turtle

# Function to draw squares
def draw_square(someone):
    for i in range(1, 5):
        someone.forward(100)
        someone.left(120)

# Function to draw art!
def draw_art():
    window = turtle.Screen()
    window.bgcolor("#a0c8f0")

    # All about Brad Square Lover
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)

    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(200)

    # All about Angie Circle Lover
    #
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)


    window.exitonclick()

draw_art()
