from Tkinter import *

root = Tk()
root.title("Nuclear Fusion Info")

logo = PhotoImage(file="sourc2.gif")
w1 = Label(root, image=logo)
w1.image = logo
w1.pack(side="right")

root.mainloop()
