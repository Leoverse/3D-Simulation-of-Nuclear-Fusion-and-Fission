from Tkinter import *

root = Tk()
root.title("Nuclear Fission Info")


logo = PhotoImage(file="source.gif")
w1 = Label(root, image=logo)
w1.image = logo
w1.pack(side="right")

root.mainloop()
