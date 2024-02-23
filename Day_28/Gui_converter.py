from tkinter import *


def miles_km_conv():
    text_value = int(input.get())
    kilo =text_value * 1.609344
    calculation.configure(text=kilo)

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)


input = Entry(width=10)
input.grid(column=3,row=1)
miles = Label(text="Miles")
miles.grid(column=4,row=1)
km = Label(text="KM")
km.grid(column=4,row=2)
text_equal = Label(text="is equal to")
text_equal.grid(column=2,row=2)
calculation=Label()
calculation.grid(column=3,row=2)

button = Button(text="Calculate",command=miles_km_conv)
button.grid(column=3,row=5)

window.mainloop()