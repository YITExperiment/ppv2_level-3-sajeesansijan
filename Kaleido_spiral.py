import turtle

from itertools import cycle
colors = cycle(['lawn green', 'hot pink','light blue', 'yellow', 'red', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.bgcolor('black')
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+10, angle+5,shift-2)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(5)
draw_circle(10,0,1)
