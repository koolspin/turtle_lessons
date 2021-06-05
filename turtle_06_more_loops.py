import turtle


def draw_box_with_offset(side, offset):
  right_angle = 90
  t.pendown()
  for x in range(4):
    t.right(right_angle)
    t.forward(side)
  t.penup()
  t.forward(offset)
  t.left(right_angle)
  t.forward(offset)
  t.right(right_angle)


# This block of code sets up the Turtle environment
t = turtle.Turtle()
t.shapesize(3,3,1)
t.shape("turtle")
t.color("blue", "blue")
t.speed("slowest")

# Here we set two variables
box_side = 200
box_offset = 10
how_many_boxes = 10

for y in range(how_many_boxes):
  draw_box_with_offset(box_side, box_offset)


# Here we wait for a click before closing the screen
t.getscreen().exitonclick()


