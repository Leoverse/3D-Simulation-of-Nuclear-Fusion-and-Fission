from Tkinter import *
import tkMessageBox

# Interface of the Nuclear Fission which controls the
# Speed of the Nuclear Fission
# and the Number of Atoms in the Fission
# using Tkinter

root = Tk()
# Header for the Menu
root.title("Menu")
# Function that starts the fission simulation (if number of atoms > 0)
# Takes the number of atoms wanted in the fusion through the slider
# Takes the speed of the reaction wanted through the slider
# Substitutes value in fission.py using the __builtin___ import
def startfission():
    root.withdraw()
    if(int(ntext.get("1.0",END))==0):
        tkMessageBox.showinfo("ERROR", "Choose a value > 0")
    else:
        root.withdraw()
        import __builtin__
        __builtin__.Natoms = int(ntext.get("1.0",END))
        __builtin__.ratex = sspeed.get()
        import projectfinal
# Starts the fusion simulation
def startfusion():
    root.withdraw()
    import fusion
# Legend for the nuclear reactions
def fusioninfo():
    window = Toplevel()
    window.title("Nuclear Fusion Info")
    logo = PhotoImage(file="C:\Users\Garnace\Desktop\Grade XI\Sciences\Data Structures & Algorithm\sourc2.gif")
    w1 = Label(window, image=logo)
    w1.image = logo
    w1.pack(side="right")
    window.mainloop()
def fissioninfo():
    window2 = Toplevel()
    window2.title("Nuclear Fission Info")
    logo2 = PhotoImage(file="C:\Users\Garnace\Desktop\Grade XI\Sciences\Data Structures & Algorithm\source.gif")
    w2 = Label(window2, image=logo2)
    w2.image = logo2
    w2.pack(side="right")
    window2.mainloop()
# Buttons that start the fusion or fission simulation    
start = Button (root,text = "START FISSION", width = 50, height = 4, command = startfission)
start.pack()
# Slider that changes the value of the speed of the reaction
sspeed = Scale(root, from_=10, to=200, orient=HORIZONTAL, length = 600, label = "Speed of Reactions")
sspeed.pack()
# Slider that changes the value of the number of atoms used
ntext = Text(root, width = 30, height = 4)
ntext.insert(INSERT, "Insert number of atoms you want in the reaction")
ntext.pack()
start2 = Button (root,text = "START FUSION", width = 50, height = 4, command = startfusion)
start2.pack()
legend = Button(root,text = "LEGEND FOR NUCLEAR FUSION", width = 50, height = 4, command = fusioninfo)
legend.pack()
legend2 = Button(root,text = "LEGEND FOR NUCLEAR FISSION", width = 50, height = 4, command = fissioninfo)
legend2.pack()


root.mainloop()
