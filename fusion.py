from visual import*
from visual.text import *

print("""Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.""")
scene = display(title="Nuclear Fusion")

class ArrayQueue:
    def __init__(self):
        self.data=[None]
        self.size=0
        self.front=0
    def __len__(self):
        return self.size
    def isempty(self):
        return self.size == 0
    def first(self):
        if self.isempty():
            raise errormessafe("Queue is empty.")
        return self.data[self.front]
    def dequeue(self):
        if self.isempty():
            raise errormessage("Queue is empty.")
        answer=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size=self.size-1
        return answer
    def resize(self,y):
        old=self.data
        self.data=[None]*y
        walk=self.front
        for k in range(0,self.size):
            self.data[k]=old[walk]
            walk=(1+walk)%len(old)
        self.front=0
    def enqueue(self,x):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avail=(self.front+self.size)%len(self.data)
        self.data[avail]=x
        self.size=self.size+1


totalenergylabel = label(pos=(0,-9,0), text="Energy Released: 0", color = color.yellow)
totalenergy = 0
x = ""
tenergy = 0
print("This nuclear reaction is yet to be sustained on Earth. This simulation \n shows the ideal nuclear fusion requirement.")

#The wall dimensions
box_length = 10
left_wall = box(pos=(-box_length,0,0),
                size=(0.1,2*box_length,0.5),
                color=color.black)
left_wall = box(pos=(box_length,0,0),
                size=(0.1,2*box_length,0.5),
                color=color.black)
top_wall = box(pos=(0,box_length,0),
                size=(2*box_length,0.1,0.5),
                color=color.black)
bottom_wall = box(pos=(0,-box_length,0),
                size=(2*box_length,0.1,2),
                color=color.cyan)

deuterium = label(pos=(-7,-5,0), text='Deuterium', color = color.blue, depth = 0.01)
nuclear = label(pos=(0,9,0), text='Nuclear Fusion', color = color.cyan)
tritium = label(pos=(7,-5,0), text='Tritium', color = color.green)
helium = label(pos=(-6,1,0), text='Product: Helium', color = color.red)
helium = label(pos=(6,1,0), text='Product: Neutron', color = color.white)





#the atoms used
h1 = sphere(pos = (-6,-8,0), radius = 0.42, color = color.blue, make_trail = False) #deuterium
h2 = sphere(pos = (6,-8,0), radius = 0.6, color = color.green, make_trail = False)    #tritium
h3 = sphere(pos = (0.03,0.04,0), radius = 0.62, color = color.red, make_trail = False) #helium
h4 = sphere(pos = (0.03,0.04,0), radius = 0.2, color = color.white, make_trail = False) #neutron

#atom launcher
deuteriumbox = box(pos = (-6,-8.5,0), axis = (3,4,0), color = color.blue, length = 4, width = 0.4, height = 0.6)
tritiumbox = box(pos = (6,-8.5,0), axis = (-3,4,0), color = color.green, length = 4, width = 0.4, height = 0.6)

#velocities of the aroms
h1.velocity = vector(3,4,0)
h2.velocity = vector(-3,4,0)
h3.velocity = vector(-3,4,0)
h4.velocity = vector(3,4,0)

#energy particles
e1 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e2 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e3 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e4 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e5 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e6 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e7 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e8 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e9 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)
e10 = sphere(pos = (0.03,0.04,0), radius = 0.1, color = color.yellow, make_trail = True, retain = 0)

#time and control variables
stop = 0
dt = 0.05
ev = 1
ecounter = 0

while 1:
    ecounter = 0
    
    #initial velocities of the explosion energy
    e1.velocity = (2,0,-1)
    e2.velocity = (1,1,2)
    e3.velocity = (1,2,-1)
    e4.velocity = (-1,2,2)
    e5.velocity = (-2,1,-1)
    e6.velocity = (-1,0,1)
    e7.velocity = (-2,-1,2)
    e8.velocity = (-1,-2,1)
    e9.velocity = (1,-2,-1)
    e10.velocity = (2,-1,0)
    
    e1.visible = False
    e2.visible = False
    e3.visible = False
    e4.visible = False
    e5.visible = False
    e6.visible = False
    e7.visible = False
    e8.visible = False
    e9.visible = False
    e10.visible = False
    h3.visible = False
    h4.visible = False
    stop = 0

    #rate at which the simulation runs
    rate(50)
    
    #displacement function
    h1.pos = h1.pos + h1.velocity*dt
    h2.pos = h2.pos + h2.velocity*dt

    #distance formula to measure collission
    x1 = h1.pos.x
    x2 = h2.pos.x
    y1 = h1.pos.y
    y2 = h2.pos.y
    d = ((x1-x2)**2+(y1-y2)**2)**(0.5)


    #condition of the collision
    if d<0.1:
        tenergy = tenergy + 17.59
        totalenergy = str(tenergy)
        energy = ArrayQueue()
        energy.enqueue(str(tenergy))
        x = energy.first()
        totalenergylabel.text = "Energy Released: " + str(x)
        while (stop==0):
            rate(50)
            h1.visible = False
            h2.visible = False
            h3.visible = True
            h4.visible = True

            #movement of the by products
            h3.pos = h3.pos + h3.velocity*dt
            h4.pos = h4.pos + h4.velocity*dt

            #explosion of energy
            e1.visible = True
            e2.visible = True
            e3.visible = True
            e4.visible = True
            e5.visible = True
            e6.visible = True
            e7.visible = True
            e8.visible = True
            e9.visible = True
            e10.visible = True
            if ecounter<2:
                e1.pos = e1.pos + e1.velocity*ev
                e2.pos = e2.pos + e2.velocity*ev
                e3.pos = e3.pos + e3.velocity*ev
                e4.pos = e4.pos + e4.velocity*ev
                e5.pos = e5.pos + e5.velocity*ev
                e6.pos = e6.pos + e6.velocity*ev
                e7.pos = e7.pos + e7.velocity*ev
                e8.pos = e8.pos + e8.velocity*ev
                e9.pos = e9.pos + e9.velocity*ev
                e10.pos = e10.pos + e10.velocity*ev
                ecounter = ecounter + 1                
            elif ecounter==2:
                e1.visible = False
                e2.visible = False
                e3.visible = False
                e4.visible = False
                e5.visible = False
                e6.visible = False
                e7.visible = False
                e8.visible = False
                e9.visible = False
                e10.visible = False
                e1.velocity = (0,0,0)
                e2.velocity = (0,0,0)
                e3.velocity = (0,0,0)
                e4.velocity = (0,0,0)
                e5.velocity = (0,0,0)
                e6.velocity = (0,0,0)
                e7.velocity = (0,0,0)
                e8.velocity = (0,0,0)
                e9.velocity = (0,0,0)
                e10.velocity = (0,0,0)
            if h3.pos.y>8:
                stop=1
                h1.visible = True
                h2.visible = True
                h3.visible = False

                #resetting of sets
                h3.pos = (0.03,0.04,0)
                h4.pos = (0.03,0.04,0)
                e1.pos = (0.03,0.04,0)
                e2.pos = (0.03,0.04,0)
                e3.pos = (0.03,0.04,0)
                e4.pos = (0.03,0.04,0)
                e5.pos = (0.03,0.04,0)
                e6.pos = (0.03,0.04,0)
                e7.pos = (0.03,0.04,0)
                e8.pos = (0.03,0.04,0)
                e9.pos = (0.03,0.04,0)
                e10.pos = (0.03,0.04,0)
        h1.pos = (-6,-8,0)
        h2.pos = (6,-8,0)
        
