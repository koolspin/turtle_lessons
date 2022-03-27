import turtle

def setup_turtle_environment():
  t = turtle.Turtle()
  t.shapesize(3,3,1)
  t.shape("turtle")
  t.color("black", "purple")
  t.speed("fast")
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
  right_angle = 10
  t.right(right_angle)


def go_left():
  right_angle = 10
  t.left(right_angle)


def go_forward():
  t.forward(40)


def go_backward():
  t.backward(40)
def turn_blue():
  t.color("black", "blue")
def turn_purple():
  t.color("black", "purple")

def turn_white_black():
  t.color("white", "black")

def turn_green():
  t.color("black", "green")

def turn_yellow():
  t.color("black", "yellow")

def turn_red():
  t.color("black", "red")
# Here we wait for a click before closing the screen
print(t)
t.getscreen().onkeypress(go_left, "Left")
t.getscreen().onkeypress(go_right, "Right")
t.getscreen().onkeypress(go_forward, "Up")
t.getscreen().onkeypress(go_backward, "Down")
t.getscreen().onkeypress(turn_purple, "p")
t.getscreen().onkeypress(turn_blue, "b")
t.getscreen().onkeypress(turn_green, "g")
t.getscreen().onkeypress(turn_yellow, "y")
t.getscreen().onkeypress(turn_white_black, "w")
t.getscreen().onkeypress(turn_red, "r")
t.getscreen().listen()
t.getscreen().exitonclick()

print(t)

