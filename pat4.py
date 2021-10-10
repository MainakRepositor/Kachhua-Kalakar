import turtle
screen=turtle.Screen()
t=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor('black')
clr=['blue','yellow']
t.pensize(4)
t.shape('turtle')
t.penup()
t.pencolor('yellow')
m=0
for i in range(12):
      m=m+1
      t.penup()
      t.setheading(-30*i+60)
      t.forward(150)
      t.pendown()
      t.forward(25)
      t.penup()
      t.forward(20)
      t.write(str(m),align="center",font=("Arial", 12, "normal"))
      if m==12:
        m=0
      t.home()
t.home()
t.setpos(0,-250)
t.pendown()
t.pensize(10)
t.pencolor('green')
t.circle(250)
t.penup()
t.setpos(150,-270)
t.pendown()
t.pencolor('red')
t.write('Clock Dial',font=("Times New Roman", 15, "bold"))
t.ht()
turtle.done() 