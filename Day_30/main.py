from tkinter import *
from tkinter import messagebox
import random
import json
#import pyperclip - this can be used for clipboard
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    n=10
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password = ""
    for i in range(n):
        password += random.choice(characters)
    password_input.delete(0)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def collect_information():
    website_entry  = website_input.get()
    email_entry = user_input.get()
    password_entry =password_input.get()
    if len(website_entry) == 0 or len(email_entry) == 0:
       messagebox.showwarning(title="Website\email",message=" field cant be empty")
    elif len(password_entry) <10:
        messagebox.showwarning(title="website",message="Password should contain atleast 10 character")
    
    
    #messagebox.showinfo(title="Message",message="Are you sure you want to add this information")
    if len(website_entry) > 0 and len(email_entry) > 0 and len(password_entry) >=10:
        dictionary ={"website":website_entry,"email":email_entry,"password":password_entry}
        is_ok =messagebox.askokcancel(title=website_entry,message=f"These are the details saves \n {dictionary} \n Do you want to save it?")
        if is_ok == True:
            with open("Day_30/password_file.txt", "a") as f:
                f.write(str(dictionary) + '\n')
            website_input.delete(0,END)
            password_input.delete(0,END)
            user_input.delete(0,END)
            messagebox.showinfo(title="Message",message=f"{website_entry} website information added to datastore ")

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Manager")
window.minsize(width=400,height=400)
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
image_pass =PhotoImage(file="Day_30\\logo.png")
canvas.create_image(100,100,image=image_pass)
canvas.grid(column =2,row=1)

website_label=Label(text="Website:")
website_label.grid(column=1,row=2)
website_input =Entry(width=35)
website_input.grid(column=2,row=2,columnspan=3)
website_input.focus()

user_label=Label(text="Email/Username:")
user_label.grid(column=1,row=3)
user_input =Entry(width=35)
user_input.grid(column=2,row=3,columnspan=3)
user_input.insert(0, 'yourname@gmail.com')

password_label=Label(text="Password:")
password_label.grid(column=1,row=4)
password_input =Entry(width=21)
password_input.grid(column=2,row=4)
#password_input.insert(0,"********")

password_button = Button(text="Generate password",command=password_generator)
password_button.grid(column=3,row=4)
#password_button.config(bg="Green", fg="white",width = "16",height="1", font=("Arial", 8),borderwidth = '2')
add_button = Button(text="Add",command=collect_information)
add_button.grid(column=2,row=5,columnspan=3)
add_button.config(bg="Green", fg="white",width = "36", font=("Arial", 8),borderwidth = '2')
window.mainloop()