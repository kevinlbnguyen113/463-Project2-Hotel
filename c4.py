from tkinter import Label, Menubutton, Tk
from tkinter import *
import array
import tkinter.messagebox

window = Tk()
window.title("Dirty Rooms")
window.geometry("850x200")
a = 0

for row in range(7):  # populate room and room types

    for column in range(6):

        if row == 0:
            lable1 = Label(text="Room Number", bg="black", fg="white", padx=3, pady=2)
            lable1.grid(row=0, column=1, sticky="nsew", padx=1, pady=1, columnspan=10)
        elif row == 0 and column == 0:
            lable0 = Label(text="")
            lable0.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)


        else:
            a += 1  # using Menu Button to let user select status of the room
            label = Menubutton(window, text=a, bg="green", fg="white", padx=1, pady=1)
            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            window.grid_columnconfigure(column, weight=1, uniform=1)
            label.menu = Menu(label)
            label["menu"] = label.menu
            label.menu.add_command(label="Housekeeper Name")
            label.menu.add_command(label="Room number")
            label.menu.add_command(label="Room Type")
            label.menu.add_command(label="Room Status")
            label.menu.add_command(label="Bathroom")
            label.menu.add_command(label="Bed Sheets")
            label.menu.add_command(label="Vacuum")
            label.menu.add_command(label="Dusting")
            label.menu.add_command(label="Electronics")


window.mainloop()