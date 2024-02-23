from tkinter import *

def change_text():
    text_value = input.get()
    my_label.configure(text=text_value)


new_window =Tk()
new_window .title("My First Gui ")
new_window .minsize(width=400,height=400)
new_window .config(padx=100,pady=100)

# adding label, packer used to layout components we are building
my_label = Label(text="My First Label")
#my_label.pack()
#my_label.place(x=0,y=90)
my_label.grid(column=2,row=1)

button_destroy = Button(new_window, text='Stop', width=25, command=new_window.destroy)
button_destroy.grid(column=4,row=1)
button = Button(text="click", width=25, command=change_text)
button.grid(column=3,row=2)
input =Entry(width=25)
input.grid(column=4,row=4)



new_window.mainloop()
