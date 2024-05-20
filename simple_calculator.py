## Simple Calculator

## Building a Simple Calculator programme with Python functions


from tkinter import *

root = Tk()
root.title = ("Simple Calculator")
v = Entry(root, width=25, borderwidth=5)
v.grid(row=0, column=0, columnspan=3, padx=25, pady=40)

def button_click(number):
    current=v.get()
    v.delete(0, END)
    v.insert(0, str(current) + str(number))
    
def clear_type():
    v.delete(0, END)
    
def button_myplus():
    first_number = v.get()
    global f_number
    global math
    math = "addition"
    f_number = int(first_number)
    v.delete(0, END)
    
def button_myminus():
    first_number = v.get()
    global f_number
    global math
    math = "subtraction"
    f_number = int(first_number)
    v.delete(0, END)
    
def button_mydivider():
    first_number = v.get()
    global f_number
    global math
    math = "division"
    f_number = int(first_number)
    v.delete(0, END)
    
def button_mytimes():
    first_number = v.get()
    global f_number
    global math
    math = "multiplication"
    f_number = int(first_number)
    v.delete(0, END)
    
    
    
def button_equal():
    my_number = v.get()
    v.delete(0, END)
    if math == "addition":
        v.insert(0, f_number+int(my_number))
    elif math =="multiplication":
        v.insert(0, f_number*int(my_number))
    elif math =="division":
        v.insert(0, f_number/int(my_number))
    elif math == "subtraction":
        v.insert(0,f_number-int(my_number))
    

button_1 = Button(root, text="1", padx=20, pady=10, command = lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command = lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command = lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command = lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command = lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command = lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command = lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command = lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command = lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command = lambda: button_click(0))
button_clear = Button(root, text="c", padx=20, pady=10, command=clear_type)
button_plus = Button(root, text="+", padx=20, pady=10, command=button_myplus)
button_minus = Button(root, text="-", padx=20, pady=10, command=button_myminus)
button_times = Button(root, text="X", padx=20, pady=10, command=button_mytimes)
button_divider = Button(root, text="/", padx=20, pady=10, command=button_mydivider)
button_equal = Button(root, text="=", padx=20, pady=10, command=button_equal)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=5, column=1)
button_plus.grid(row=4, column=0)
button_minus.grid(row=4, column=2)
button_times.grid(row=4, column=1)
button_divider.grid(row=5, column=0)
button_equal.grid(row=5, column=2)
button_clear.grid(row=6, column=1)

root.mainloop()

