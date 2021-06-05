import turtle


# This block of code sets up the Turtle environment
t = turtle.Turtle()
t.shapesize(3,3,1)
t.shape("turtle")
t.color("blue", "blue")
t.speed("slowest")

# Here we set two variables
box_side = 200
right_angle = 90

# To Draw a box, using a for loop
for x in range(4):
  t.right(right_angle)
  t.forward(box_side)

# Here we wait for a click before closing the screen
t.getscreen().exitonclick()


