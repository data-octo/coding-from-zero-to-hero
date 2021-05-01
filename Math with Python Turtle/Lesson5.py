import turtle

def draw_cross(pen):
    for i in range(4):
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.left(90)

pen = turtle.Turtle()

pen.color('purple')

# starting_pos = [(200, 200), (200+50, 200-100), (200+150, 200-50), (200+100, 200+50)]


for _ in range(8):
    pen.penup()
    pen.left(90)
    pen.forward(100)
    pen.pendown()
    draw_cross(pen)
    if _ == 3:
        pen.penup()
        pen.goto(pen.xcor()+20, pen.ycor()+50)
        pen.left(45)
        pen.pendown()

# x, y = pen.pos()
# pen.goto(x+50, y-50)
# draw_cross(pen)

turtle.done()
