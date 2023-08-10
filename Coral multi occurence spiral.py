import turtle
import math

screen = turtle.Screen()
screen.title('Hexagon Spiral of Hexagon Spirals - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)

colors = [ 'red', 'orange', 'green', 'teal', 'blue', 'magenta' ]

def draw_spiral(x,y,r,direction,first=False):
    if r < 1: return
    d = direction
    r_ratio = math.cos(math.radians(30))/math.cos(math.radians(30-alpha))
    d_ratio = math.sin(math.radians(30))-r_ratio*math.sin(math.radians(30-alpha))
    for i in range(6):
        if first: turtle.color(colors[i]) 
        px = x + r*math.cos(math.radians(direction))
        py = y + r*math.sin(math.radians(direction))
        r2 = r
        d = direction
        c = 0
        flag = False
        while True:
            dist = r2*d_ratio
            if c > 10 and dist < 1: break
            if dist > 4:
                draw_spiral(px,py,dist*0.4,d)
                turtle.up()
                turtle.goto(px,py)
                turtle.seth(d+180-60)
                turtle.fd(dist)
                px,py = turtle.xcor(), turtle.ycor()
            elif not flag:
                turtle.up()
                turtle.goto(px,py)
                turtle.down()
                flag = True
                turtle.seth(d+180-60)
                turtle.fd(dist)
            else:   
                turtle.seth(d+180-60)
                turtle.fd(dist)
    
            r2 = r2*r_ratio
            d += alpha
            c += 1
        direction += 60
    
    
alpha = 20
draw_spiral(0,0,800,90,True)
screen.update()
ts=turtle.getscreen()
ts.getcanvas().postscript(file = "spiral.eps")
