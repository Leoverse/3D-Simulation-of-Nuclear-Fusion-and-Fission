from visual import *
from random import random
from random import randint
from math import hypot
import random
from Tkinter import *

#import nuclearfission
#exec(open("nuclearfission.py").read())

# Instructions on operating the Simulation
print("""Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.""")

scene = display(title="Nuclear Fission")

# Size of the container for the Fission Reaction 
side = 10.
# Thickness of the sides of the container
thk = 0.3 
s2 = 2*side - thk
s3 = 2*side + thk
# Properties of the container, a side of the container is made up of box objects
wallR = box (pos=( side, 0, 0), size=(thk, s2, s3),  color = color.white, opacity=0.2)
wallL = box (pos=(-side, 0, 0), size=(thk, s2, s3),  color = color.white, opacity=0.2)
wallB = box (pos=(0, -side, 0), size=(s3, thk, s3),  color = color.white, opacity=0.2)
wallT = box (pos=(0,  side, 0), size=(s3, thk, s3),  color = color.white, opacity=0.2)
wallBK = box(pos=(0, 0, -side), size=(s2, s2, thk), color = color.white, opacity=0.2)

# Number of atoms present in the simulation
# Radii of the atoms used in the simulation
Ratom=0.6
Rneutron=0.4

# Mass of the atoms to be used for scaling purposes
# Muranium = 3.95256236E-25, mass of uranium
# Mstrontium = 1.45496408E-25, mass of strontium
# Mxenon = 2.18017118E-25, mass of xenon
# Mneutron = 1.67492721E-27, mass of neutron

# Array that will contain the sphere objects and it's respective properties
# specifically the appearance, position, mass, radius, and velocity of the object
Atoms = []
poslist = []
mlist = []
rlist = []
vlist = []

# Loop that creates a number of atoms specified by the user (Natoms)
# The properties of the atoms are stored in the respective arrays
# The atoms are randomly placed, given a specific radius and mass based on what atom is used
# The velocity of the atoms is generated randomly, rounded off to the tenths place (1.1, 6.7, etc.)
for i in range(Natoms):
    a = round(random.uniform(-1,1),1)
    b = round(random.uniform(-1,1),1)
    c = round(random.uniform(-1,1),1)
    x = round(random.uniform(-10,10),1)
    y = round(random.uniform(-10,10),1)
    z = round(random.uniform(-10,10),1)
    r = Ratom
    rr = Rneutron
# The first atom added is the neutron which will be responsible for triggering the first fission
# The atoms are color coded, yellow for neutrons, cyan for uranium atoms, green for xenon atoms, and red for strontium atoms
    if i == 0:
        Atoms.append(sphere(pos=(x,y,z), radius=rr, color=color.yellow,
                    retain=100))
        mlist.append(0.2)
        vlist.append(vector(a,b,c))
        rlist.append(rr)
    else:
        Atoms.append(sphere(pos=(x,y,z), radius=r, color=color.cyan))
        mlist.append(3.9)
        vlist.append(vector(0,0,0))
        rlist.append(r)
    poslist.append((x,y,z))

# Adjusted side of the container in order to disallow atoms to exceed the boundaries of the container
side = side - thk*0.5 - rlist[0]
# dt is the time interval for the simulation
dt = 0.5
# time starts at 0 seconds
t = 0.0
while True:
  # The rate describes how fast/slow the simulation will run
  rate(ratex)
  # t describes the current time frame of the simulation
  t = t + dt
  # atomc is the nth atom in the array Arrays[]
  atomc = 0
  # A loop that disallows the atoms from extending the bounds of the container, as well as giving the atoms movement
  while(atomc<len(Atoms)-1): 
      plusv = Atoms[atomc].pos + (vlist[atomc]/mlist[atomc])*dt
      plusv.x = round(plusv.x,1)
      plusv.y = round(plusv.y,1)
      plusv.z = round(plusv.z,1)
      if not (side > plusv.x > -side):
          vlist[atomc].x = -vlist[atomc].x
      if not (side > plusv.y > -side):
          vlist[atomc].y = -vlist[atomc].y
      if not (side > plusv.z > -side):
          vlist[atomc].z = -vlist[atomc].z
      Atoms[atomc].pos = plusv
      atomc = atomc + 1
  count = 0
  count2 = 1
  # A loop that determines whether a collision has occured between the atoms
  while count <= len(Atoms):
    if(count2 <= len(Atoms)):
        if count2>len(Atoms)-1 or count>len(Atoms)-1:
            count2 = 0
            count2 = 0
            break
        # vecd, dist, and colrad are components of the distance formula to calculate the distance between the centers of the two atoms used
        vecd = Atoms[count2].pos-Atoms[count].pos
        dist= sqrt(vecd.x**2+vecd.y**2+vecd.z**2)
        colrad = (rlist[count2]+rlist[count])
        # Condition that checks whether the distance between the atoms are close enough to be classified as having "collided"
        if(dist<colrad):
            # If a neutron and uranium atom collide, fission will occur
            # Producing a two (2) neutrons, a xenon atom, and a strontium atom, which will be displayed accordingly with their respective properties
            if(mlist[count]+mlist[count2]==4.1):
                d1 = (Atoms[count2].x + Atoms[count].x)/2
                e1 = (Atoms[count2].y + Atoms[count].y)/2
                f1 = (Atoms[count2].z + Atoms[count].z)/2
                d = round(d1,1)
                e = round(e1,1)
                f = round(f1,1)
                g = round(random.uniform(-1,1),1)
                h = round(random.uniform(-1,1),1)
                i = round(random.uniform(-1,1),1)
                j = round(random.uniform(-1,1),1)
                k = round(random.uniform(-1,1),1)
                l = round(random.uniform(-1,1),1)
                Atoms.append(sphere(pos=(d-1,e-1,f-1), radius=rr, color=color.yellow))
                mlist.append(0.2)
                vlist.append(vector(g,h,i))
                rlist.append(rr)
                poslist.append((d-1,e-1,f-1))
                Atoms.append(sphere(pos=(d+1,e+1,f+1), radius=rr, color=color.yellow))
                mlist.append(0.2)
                vlist.append(vector(j,k,l))
                rlist.append(rr)
                poslist.append((d+1,e+1,f+1))
                Atoms.append(sphere(pos=(d+2,e+2,f+2), radius=r, color=color.green))
                mlist.append(2.2)
                rlist.append(r)
                vlist.append(vector(0,0,0))
                poslist.append((d+2,e+2,f+2))
                Atoms.append(sphere(pos=(d-2,e-2,f-2), radius=r, color=color.red))
                mlist.append(1.5)
                vlist.append(vector(0,0,0))
                rlist.append(r)
                poslist.append((d-2,e-2,f-2))
                # The atoms in the fission process are then "used up" and deleted
                if(mlist[count]==0.2 or mlist[count2]==0.2):
                    print("!!!!!!!")
                    Atoms[count].visible = False
                    del Atoms[count]
                    del mlist[count]
                    del poslist[count]
                    del rlist[count]
                    del vlist[count]
                    Atoms[count2].visible = False
                    del Atoms[count2]
                    del mlist[count2]
                    del poslist[count2]
                    del rlist[count2]
                    del vlist[count2]
    count2 = count2+1          
    while(atomc<len(Atoms)-1): 
      plusv = Atoms[atomc].pos + (vlist[atomc]/mlist[atomc])*dt
      plusv.x = round(plusv.x,1)
      plusv.y = round(plusv.y,1)
      plusv.z = round(plusv.z,1)
      if not (side > plusv.x > -side):
          vlist[atomc].x = -vlist[atomc].x
      if not (side > plusv.y > -side):
          vlist[atomc].y = -vlist[atomc].y
      if not (side > plusv.z > -side):
          vlist[atomc].z = -vlist[atomc].z
      Atoms[atomc].pos = plusv
      atomc = atomc + 1


