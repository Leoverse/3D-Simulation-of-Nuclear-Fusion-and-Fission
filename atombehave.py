from visual import *

ball1 = sphere(pos = vector (0,0,0), radius = 0.5, color = color.green)


r = vector(0,0,0)

while r.y < 2:
    rate(10)
    ##sphere(pos= r, radius=0.5, color=color.cyan)
    ball1.pos = r
    ##r.x = r.x + 1
    r.y = r.y + 0.1
    ##r.z = r.z + 1


print('end of program')
 
