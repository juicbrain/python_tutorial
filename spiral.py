from turtle import *
colors = ["red","cyan","green","yellow","pink","purple","yellow"]
bgcgffrolor("black")
speed(0)
for x in range(200):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)

hideturtle()

done()