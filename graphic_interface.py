from tkinter import *
root = Tk()
mylabel = Label(root, text ="Hello World")
mylabel.pack()
root.mainloop()


from tkinter import *
root = Tk()
mylabel = Label(root, text ="Hello World")
mylabel2 = Label(root, text ="Learning about GUI")
mylabel3 = Label(root, text ="Python Class")
mylabel.grid(row=0, column=1)
mylabel2.grid(row=0, column=2)
mylabel3.grid(row=0, column=3)
root.mainloop()


root = Tk()
def my_click():
    my_label = Label(root, text="I just clicked this button")
    my_label.pack()
    
my_button = Button(root, text="Click Me!", command=my_click, fg="blue", bg="green")
my_button.pack()
root.mainloop()


root = Tk()
my_input = Entry(root)
my_input.insert(0, "Enter your Username")
my_input.pack()
def you_click():
    hello = "Hello" + my_input.get()
    my_label = Label(root, text=hello)
    my_label.pack()
    
my_button = Button(root, text= "Enter your name", command=you_click, fg="blue", bg="green")
my_button.pack()
root.mainloop()
