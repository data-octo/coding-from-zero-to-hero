#2D Shapes using Python Turtle - www.101computing.net/2D-shapes-using-python-turtle/
import turtle
myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("red")
# myPen.delay(5) #Set the speed of the turtle

#A Procedue to draw any regular polygon with 3 or more sides.
def drawPolygon(numberOfsides):
  exteriorAngle=360/numberOfsides
  length=600/numberOfsides
  myPen.penup()
  myPen.goto(-length/2,-length/2)
  myPen.pendown()
  for i in range(0,numberOfsides):
      myPen.forward(length)
      myPen.left(exteriorAngle)
  myPen.hideturtle()

#Main Program Starts Here
sides = int(input("Number of sides for your shape?"))
drawPolygon(sides)

turtle.done()