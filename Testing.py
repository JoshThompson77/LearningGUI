from tkinter import *

root = Tk()

r = IntVar()
r.set(2)

def printvalue(value):
    print(value)


b1 = Radiobutton(root, text= 'Here', variable= r, value= 1, command= lambda: printvalue(r.get())).pack()
b2 = Radiobutton(root, text= 'now', variable = r, value = 2, command= lambda: printvalue(r.get())).pack()


root.mainloop()