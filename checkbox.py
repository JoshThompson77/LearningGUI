from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title("CheckBoxes")
root.geometry("400x400")

var = IntVar()

c = Checkbutton(root, text="Check me Please", variable=var)
c.pack()


root.mainloop()