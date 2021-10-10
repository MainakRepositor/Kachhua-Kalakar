# import turtle library
import turtle             
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.color("black")
my_pen.setx(-200)
my_pen.sety(-200)
def my_sqrfunc(size):
   for i in range(4):
      my_pen.fd(size)
      my_pen.left(90)
      size = size - 5
for i in range(20):
    my_sqrfunc(466 - (i * 22))



turtle.done()