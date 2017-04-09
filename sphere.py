from visual import *

ball1 = sphere(pos = vector (0,0,0), radius = 0.5, color = color.green)
ball2 = sphere(pos = vector (-3,4,0), radius = 0.5, color = color.cyan)
pointer = arrow(pos = vector(0,0,0), axis = ball2.pos - ball1.pos, color = color.red)

r = vector(-3,4,0)

while r.x < 10:
    rate(10)
    ##sphere(pos= r, radius=0.5, color=color.cyan)
    ball2.pos = r
    r.x = r.x + 1

print('end of program')
 
