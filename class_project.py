# from tkinter import *

# root = Tk()
# mylabel = Label(root, text="Hello Tkinter")
# mylabel.pack()
# # # mylabel.grid(row=1, column=2, padx=10, pady=10)
# root.mainloop()

# root = Tk()
# my_input = Entry(root)
# my_input.insert(0, "Enter your username")
# my_input.pack()




# def you_click():
#     hello = "Hello" + (" ") + my_input.get()
#     my_label = Label(root, text= "click me")
#     my_label.pack()


# my_button = Button(root, text= "Click me", command= you_click, fg= "blue", bg = "green")
# my_button.pack()
# root.mainloop()


# root = Tk()
# def you_click():
#     my_label = Label(root, text= "clicked")
#     my_label.pack()


# my_button = Button(root, text= "Click me", command= you_click, fg= "blue", bg = "green")
# my_button.pack()
# root.mainloop()

import tkinter as tk 


def mydrawing():
    root = tk.Tk()
    root.title = ("my canva")
    mycanva= tk.Canvas(root, bg = "white", width= 500, height=500)
    mycanva.pack()

    x,y = None, None 
    

    def mybuttondrag(e):
        x, Y
        x, y = e.x, e.y


    root.mainloop()

mydrawing()