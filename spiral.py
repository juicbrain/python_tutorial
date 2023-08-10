# importing turtle module
import turtle

# number of side
sides = 5

# size
n = 7

# creating instance of turtle
pen = turtle.Turtle()

# loop to draw a side
for i in range(n * sides):
    # drawing side of
    # length i*10
    pen.forward(i * 10)

    # changing direction of pen
    # by 360/sides degree in clockwise
    pen.right(360 / sides)

# closing the instance
turtle.done()
