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

# for y in range(how_many_boxes):
#   draw_box_with_offset(t, box_side, box_offset)


def go_right():
  right_angle = 90
  t.right(right_angle)


def go_left():
  right_angle = 90
  t.left(right_angle)


def go_forward():
  t.forward(200)


def go_backward():
  t.backward(200)


# Here we wait for a click before closing the screen
print(t)
t.getscreen().onkeypress(go_left, "Left")
t.getscreen().onkeypress(go_right, "Right")
t.getscreen().onkeypress(go_forward, "Up")
t.getscreen().onkeypress(go_backward, "Down")
t.getscreen().listen()
t.getscreen().exitonclick()


