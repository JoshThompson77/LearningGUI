from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=25, borderwidth=5)
e.grid(column=0, row = 0, columnspan =3, padx =10, pady = 10)


def myclick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()

def button_add(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def button_clear():
    e.delete(0, END)

def button_addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    global s_num
    s_num = int(second_number)

    if math == "addition":
        final_number = s_num + f_num
        e.delete(0, END)
        e.insert(0, final_number)

    elif math == "subtraction":
        final_number = f_num - s_num
        e.delete(0, END)
        e.insert(0, final_number)
    elif math == "multiplication":
        final_number = f_num * s_num
        e.delete(0, END)
        e.insert(0, final_number)
    else:
        final_number = f_num / s_num
        e.delete(0, END)
        e.insert(0, final_number)


    e.delete(0, END)
    e.insert(0, final_number)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#Define buttons
button_1 = Button(root, text = "1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(root, text = "2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(root, text = "3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(root, text = "4", padx=40, pady=20, command= lambda: button_add(4))
button_5 = Button(root, text = "5", padx=40, pady=20, command= lambda: button_add(5))
button_6 = Button(root, text = "6", padx=40, pady=20, command= lambda: button_add(6))
button_7 = Button(root, text = "7", padx=40, pady=20, command= lambda: button_add(7))
button_8 = Button(root, text = "8", padx=40, pady=20, command= lambda: button_add(8))
button_9 = Button(root, text = "9", padx=40, pady=20, command= lambda: button_add(9))
button_0 = Button(root, text = "0", padx=40, pady=20, command= lambda: button_add(0))
button_ad = Button(root, text = "+", padx=40, pady=20, command=button_addition)
button_equal = Button(root, text = "=", padx=87, pady=20, command=button_equal)
button_clear = Button(root, text = "Clear", padx=75, pady=20, command= button_clear)

button_subtract = Button(root, text = "-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text = "x", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text = "/", padx=40, pady=20, command=button_divide)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_ad.grid(row=5, column = 0)
button_clear.grid(row=4, column=1, columnspan = 2)
button_equal.grid(row=5, column=1, columnspan =2)

button_substract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

myButton = Button(root, text ="Click Me", command=myclick)


root.mainloop()