import turtle

sc= turtle.Screen()

sc.bgcolor('black')


my_pencil = turtle.Turtle()

my_pencil.speed(0) # adjust speed with 0 being the highest

my_pencil.pensize(3) #pensize is the thickness


colors_list = ['Red','Orange','Yellow','Green','Blue','Indigo','Violet']

for i in range(4): # in one iteration we are creating different squares of above mentioned colors

    for colour in colors_list:

        my_pencil.color(colour)

        my_pencil.left(12) #turn 12deg

        for j in range(4): # 1 square created

            my_pencil.forward(200)

            my_pencil.left(90)
            
turtle.done() # this is to keep the window open