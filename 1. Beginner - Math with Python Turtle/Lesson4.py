# myturtle.py
from turtle import * 

# def triangle(sidelength=100):
#     for i in range(3):
#         forward(sidelength)
#         right(60)

# triangle()

length = 200

left(180)
forward(200)
write('120')
forward(length)
write('60', align='left')
right(120)
forward(length)
write('60', align='left')
right(120)
forward(length)
write('60', move=True, align='right')
hideturtle()

done()
