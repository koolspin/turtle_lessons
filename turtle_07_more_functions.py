import turtle


def setup_turtle_environment():
  t = turtle.Turtle()
  t.shapesize(3,3,1)
  t.shape("turtle")
  t.color("blue", "blue")
  t.speed("slowest")
  return t


def draw_box_with_offset(tur, side, offset):
  right_angle = 90
  tur.pendown()
  for x in range(4):
    tur.right(right_angle)
    tur.forward(side)
  tur.penup()
  tur.forward(offset)
  tur.left(right_angle)
  tur.forward(offset)
  tur.right(right_angle)


t = setup_turtle_environment()

# Here we set two variables
box_side = 200
box_offset = 10
how_many_boxes = 10

for y in range(how_many_boxes):
  draw_box_with_offset(t, box_side, box_offset)


# Here we wait for a click before closing the screen
t.getscreen().exitonclick()


