from visual import *

print("""
Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.
""")

side = 4.0
side2 = 4.0
side3 = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
wallR = box (pos=( side, 0, 0), size=(thk, s2, s3),  color = color.red)
wallL = box (pos=(-side, 0, 0), size=(thk, s2, s3),  color = color.red)
wallB = box (pos=(0, -side, 0), size=(s3, thk, s3),  color = color.blue)
wallT = box (pos=(0,  side, 0), size=(s3, thk, s3),  color = color.blue)
wallBK = box(pos=(0, 0, -side), size=(s2, s2, thk), color = (0.7,0.7,0.7))

ball = sphere (color = color.red, radius = 0.4, retain=200)
##ball = sphere (color = color.red, radius = 0.4, make_trail=True, retain=200)
##ball.trail_object.radius = 0.05
ball.mass = 1.0
ball.p = vector (-0.15, -0.23, +0.27)

side = side - thk*0.5 - ball.radius

dt = 0.5
t=0.0

ball2 = sphere (color = color.green, radius = 0.4, retain=200)
##ball2.trail_object.radius = 0.05
ball2.mass = 1.0
ball2.p = vector (-0.30, -0.12, +0.14)

side2 = side2 - thk*0.5 - ball2.radius

dt2 = 0.5
t2=0.0

ball3 = sphere (color = color.blue, radius = 0.4, retain=200)
##ball3.trail_object.radius = 0.05
ball3.mass = 1.0
ball3.p = vector (-0.45, -0.35, +0.41)

side3 = side3 - thk*0.5 - ball3.radius

dt3 = 0.5
t3=0.0
while True:
  rate(100)
  t = t + dt
  ball.pos = ball.pos + (ball.p/ball.mass)*dt
  if not (side > ball.x > -side):
    ball.p.x = -ball.p.x
  if not (side > ball.y > -side):
    ball.p.y = -ball.p.y
  if not (side > ball.z > -side):
    ball.p.z = -ball.p.z
  t2 = t2 + dt2
  ball2.pos = ball2.pos + (ball2.p/ball2.mass)*dt2
  if not (side2 > ball2.x > -side2):
    ball2.p.x = -ball2.p.x
  if not (side2 > ball2.y > -side2):
    ball2.p.y = -ball2.p.y
  if not (side2 > ball2.z > -side2):
    ball2.p.z = -ball2.p.z
  t3 = t3 + dt3
  ball3.pos = ball3.pos + (ball3.p/ball3.mass)*dt3
  if not (side3 > ball3.x > -side3):
    ball3.p.x = -ball3.p.x
  if not (side3 > ball3.y > -side3):
    ball3.p.y = -ball3.p.y
  if not (side3 > ball3.z > -side3):
    ball3.p.z = -ball3.p.z





