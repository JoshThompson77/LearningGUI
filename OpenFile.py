from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Opening Files?')



def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir=('/Users/josh/Desktop/Monzyk Innovations'),
                                               title='Select a File', filetypes=[("excel files", "*.png")])
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


mine = Button(root, text = "Open File", command=open).pack()



root.mainloop()