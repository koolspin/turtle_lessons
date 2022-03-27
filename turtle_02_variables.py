import turtle


# This block of code sets up the Turtle environment
t = turtle.Turtle()
t.shapesize(3,3,1)
t.shape("turtle")
t.color("blue", "blue")
t.speed("slowest")

# Here we set two variables
box_side = 400
right_angle = 90

# To Draw a box:
t.right(right_angle)
t.forward(box_side)
t.right(right_angle)
t.forward(box_side)
t.right(right_angle)
t.forward(box_side)
t.right(right_angle)
t.forward(box_side)

# Here we wait for a click before closing the screen
t.getscreen().exitonclick()


