from tkinter import  Label, Menubutton, Tk
from tkinter import *
import array
import tkinter.messagebox


window= Tk()
window.title("Room Type")
window.geometry("850x200")
a=99#set room to start at 99 then add 1 to make 100 initial starting room

#function to change color depends on status of the room
def availableRoom(row,column):
    #print(label.grid_info())
    widget= window.grid_slaves(row=row, column=column)[0]
    widget.configure(bg="green")
def dirtyRoom(row,column):
    #print(label.grid_info())
    widget= window.grid_slaves(row=row, column=column)[0]
    widget.configure(bg="pink",fg="black")
def occupiedRoom(row,column):
    #print(label.grid_info())
    widget= window.grid_slaves(row=row, column=column)[0]
    widget.configure(bg="blue",fg="black")
def maintenanceRoom(row,column):
    #print(label.grid_info())
    widget= window.grid_slaves(row=row, column=column)[0]
    widget.configure(bg="red",fg="white")

for row in range (7):#populate room and room types
    

    for column in range (6):
        
        if row == 0 :
            lable1 = Label(text="Room Number",bg="black",fg="white",padx= 3,pady=3)
            lable1.grid(row=0,column=1,sticky= "nsew",padx= 1,pady=1,columnspan=8)    
        elif row == 0 and column==0:
            lable0= Label(text="")
            lable0.grid(row=0, column=0,sticky= "nsew",padx= 1,pady=1)

        elif column == 0 and row ==1:
            lable2=Label(text="King Size bed",bg="black",fg="white",padx= 3,pady=3)
            lable2.grid(row=1, column=0,sticky= "nsew",padx= 1,pady=1)
        elif column == 0 and row ==2:
            lable3=Label(text="Double Queen Bed",bg="black",fg="white",padx= 3,pady=3)
            lable3.grid(row=2, column=0,sticky= "nsew",padx= 1,pady=1)
        elif row ==3 and column==0:
            lable4=Label(text="Double Queen Bed With Kitchen",bg="black",fg="white",padx= 3,pady=3)
            lable4.grid(row=3, column =0,sticky= "nsew",padx= 1,pady=1)
        elif row ==4 and column==0:
            lable5=Label(text="Suite",bg="black",fg="white",padx= 3,pady=3)
            lable5.grid(row=4, column =0,sticky= "nsew",padx= 1,pady=1)
        elif row == 5 :
            label6= Label(text= "Key", bg="Gray", fg="white",padx=3,pady=3,font="24")
            label6.grid(row=5, column= 1,sticky= "nsew",padx= 1,pady=1, columnspan= 6)
        elif row== 6 :
            labelG= Label(text= "Available", bg="green", fg="white")
            labelG.grid(row=6, column= 1,sticky= "nsew",padx= 0,pady=1,columnspan=1)
            labelG= Label(text= "Occupied", bg="blue", fg="white")
            labelG.grid(row=6, column= 2,sticky= "nsew",padx= 0,pady=1,columnspan=1)
            labelG= Label(text= "Dirty", bg="pink", fg="black")
            labelG.grid(row=6, column= 3,sticky= "nsew",padx= 00,pady=1,columnspan=1)
            labelG= Label(text= "Maintenance", bg="red", fg="black")
            labelG.grid(row=6, column= 4,sticky= "nsew",padx= 0,pady=1,columnspan=2)
        
        
        else:  
            a+=1  #using Menu Button to let user select status of the room
            label = Menubutton(window, text=a,bg="green",fg="white",padx= 1,pady=1)
            label.grid(row=row, column= column,sticky= "nsew",padx= 1,pady=1)
            window.grid_columnconfigure(column, weight= 1, uniform =1)
            label.menu= Menu (label)
            label["menu"]= label.menu
            label.menu.add_command (label = "available",command=lambda  row= row, column=column: availableRoom(row,column))
            label.menu.add_command (label = "occupied", command=lambda  row= row, column=column : occupiedRoom(row,column))
            label.menu.add_command (label = "dirty", command=lambda  row= row, column=column: dirtyRoom(row,column))
            label.menu.add_command (label = "maintenance", command=lambda  row= row, column=column: maintenanceRoom(row,column))


            
            
window.mainloop()