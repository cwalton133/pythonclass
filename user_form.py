
## User Form Management

from tkinter import *
import sqlite3
from tkinter import messagebox

def create_table():
    tunde = sqlite3.connect("user.db")
    cursor = tunde.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        )
        """)
    tunde.commit()
    tunde.close()

def save_credentials():
    email = email_entry.get()
    password = password_entry.get()
    
    if email == password:
        tunde = sqlite3.connect("user.db")
        cursor = tunde.cursor()
        cursor.execute("INSERT INTO credentials VALUES(NULL,?,?)", (email, password))
        tunde.commit()
        tunde.close()
        
        messagebox.showinfo("Success", "Credential save successfully")
    else:
        messagebox.showwarning("Error", "Error in creating Credentials")


def display_credentials(): 
    tunde = sqlite3.connect("user.db") 
    cursor = tunde.cursor() 
    cursor.execute("SELECT * FROM credentials") 
    data =cursor.fetchall() 
    tunde.close() 
    if data: 
        result_text.delete(1.0, END) 
        for i in data: 
            result_text.insert(END, f'Email: {i[1]}\nPassword: {i[2]}n\n') 
    else:
        result_text.delete(1.0, END) 
        messagebox.showwarning("Error", "Error in creating Credentials") 
        result_text.delete(END, "Data not found") 

root = Tk()
root.title("Email and Password Management")
create_table()

email_label = Label(root, text="Enter Email Address") 
email_label.grid(row=0, column=0, padx=10, pady=10) 
email_entry = Entry(root) 
email_entry.grid(row=0, column=1, padx=10, pady=10) 


password_label = Label(root, text="Enter your Password") 
password_label.grid(row=1, column=0, padx=10, pady=10) 
password_entry = Entry(root, show="*") 
password_entry.grid(row=1, column=1, padx=10, pady=10) 

save_button = Button(root, text="Save Credentials", command=save_credentials) 
save_button.grid(row=2, column=0, columnspan=2, pady=10) 

display_button = Button(root, text="Displaying Credentials", command=display_credentials) 
display_button.grid(row=3, column=0, columnspan=2, pady=10) 

result_text = Text(root, height=10, width=40) 
result_text.grid(row=4, column=0, columnspan=3, pady=10) 

root.mainloop()









