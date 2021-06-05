# Copy and paste this to get the session started
# These commands can be copy / pasted into an interactive python shell
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.shapesize(3,3,1)
t.shape("turtle")
t.color("blue", "blue")

# These commands tell the turtle what to do:

# Tell the turtle to turn 90 degrees to his right:
t.right(90)

# Tell the turtle to turn 45 degrees to his left:
t.left(45)

# Tell the turtle to turn in the opposite direction:
t.right(180)

# Tell the turtle to move forward 100 pixels (from wherever he is)
t.forward(100)

# Draw a circle with a radius of 50 pixels
t.circle(50)

# To Draw a box:
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# Change the color of the pen
t.color("green")

# Bring the turtle back to the center
t.home()

# Erase everything the turtle has drawn
t.clear()



