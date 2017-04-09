from visual import *

scene = display(width = 600, height = 600, center = (0,5,0))

Sun = sphere(pos = (0,0,0), radius = 100, color = color.orange)
earth = sphere(pos = (-200,0,0), radius = 10, material = materials.earth, make_trail = true)
earth1 = sphere(pos = (-200,150,0), radius = 10, material = materials.earth, make_trail = true)
earth2 = sphere(pos = (0,200,0), radius = 10, material = materials.earth, make_trail = true)
earth3 = sphere(pos = (200,150,0), radius = 10, material = materials.earth, make_trail = true)

earthv = vector(0,0,5)
earth1v = vector(0,0,5)
earth2v = vector(0,0,5)
earth3v = vector(0,0,5)

for i in range(1000):
    rate(100)
    earth.pos = earth.pos + earthv
    dist = (earth.x**2 + earth.y**2 + earth.z**2)**0.5
    RadialVector = (earth.pos - Sun.pos)/dist
    Fgrav = -10000*RadialVector/dist**2
    earthv = earthv + Fgrav
    earth.pos += earthv
    if dist <= Sun.radius: break
    earth2.pos = earth2.pos + earth2v
    dist2 = (earth2.x**2 + earth2.y**2 + earth2.z**2)**0.5
    RadialVector2 = (earth2.pos - Sun.pos)/dist2
    Fgrav2 = -10000*RadialVector2/dist2**2
    earth2v = earth2v + Fgrav2
    earth2.pos += earth2v
    if dist2 <= Sun.radius: break
    earth1.pos = earth1.pos + earth1v
    dist1 = (earth.x**2 + earth.y**2 + earth.z**2)**0.5
    RadialVector1 = (earth1.pos - Sun.pos)/dist1
    Fgrav1 = -10000*RadialVector1/dist1**2
    earth1v = earth1v + Fgrav1
    earth1.pos += earth1v
    if dist1 <= Sun.radius: break
    earth3.pos = earth3.pos + earth3v
    dist3 = (earth.x**2 + earth.y**2 + earth.z**2)**0.5
    RadialVector3 = (earth3.pos - Sun.pos)/dist3
    Fgrav3 = -10000*RadialVector3/dist3**2
    earth3v = earth3v + Fgrav3
    earth3.pos += earth3v
    if dist3 <= Sun.radius: break
