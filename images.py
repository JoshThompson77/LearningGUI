from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Images")

myImg = ImageTk.PhotoImage(Image.open("/Users/josh/Desktop/IMG_5157.jpeg"))
myLabel = Label(image=myImg)
myLabel.pack()

button_1 = Button(root, text = "1", padx=40, pady=20, command=lambda: button_add(1))
button_quit= Button(root, text= "Exit", command=root.quit)
button_quit.pack()


root.mainloop()

