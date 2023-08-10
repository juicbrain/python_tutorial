import turtle

t = turtle.Turtle()
colors = ['red', 'blue', 'orange', 'green', 'black', 'brown']
t.pensize(20)

t.goto(0,150)
t.right(90)
t.color('gray')
t.forward(470)

t.pensize(3)

t.penup()
t.goto(0,150)
t.pendown()

for i in range(10):
    t.color(colors[i%6])
    t.forward(200)
    t.right(120)
    t.forward(40)
    t.goto(0,150)
    t.fillcolor("black")
    t.left(84)



turtle.done()
