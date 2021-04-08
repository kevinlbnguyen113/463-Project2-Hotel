from tkinter import  Label, Menubutton, Tk, Scrollbar
from tkinter import *
import array
import tkinter.messagebox
from datetime import *
import calendar
import datetime
currentDate= datetime.datetime.now()
currentDay= date.today()#current date for schedule
nextDay1=date.today() + datetime.timedelta(days=1)
nextDay2=date.today() + datetime.timedelta(days=2)
nextDay3=date.today() + datetime.timedelta(days=3)
nextDay4=date.today() + datetime.timedelta(days=4)
nextDay5=date.today() + datetime.timedelta(days=5)
nextDay6=date.today() + datetime.timedelta(days=6)
nextDay7=date.today() + datetime.timedelta(days=7)

year = currentDate.year
day= currentDate.day
month= currentDate.month


window= Tk()
window.title("Available rooms")
window.geometry("950x600")

a=99

for row in range (22):

    for column in range (9):

        if row == 0 :  #day of the week
            lable0= Label(text="Room Number",bg="black",fg="white",padx= 3,pady=3)
            lable0.grid(row=0, column=0,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=currentDay.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=1,sticky= "nsew",padx= 1,pady=1)
            lable4 = Label(text=nextDay1.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable4.grid(row=0, column=2,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=nextDay2.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=3,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=nextDay3.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=4,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=nextDay4.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=5,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=nextDay5.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=6,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=nextDay6.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=7,sticky= "nsew",padx= 1,pady=1)
            lable3 = Label(text=nextDay7.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
            lable3.grid(row=0, column=8,sticky= "nsew",padx= 1,pady=1)
        elif row == 1:#date
            lable2= Label(text=str(currentDay.month) +"/" + str(currentDay.day))
            lable2.grid(row= 1, column= 1,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay1.month) +"/" + str(nextDay1.day))
            lable2.grid(row= 1, column= 2,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay2.month) +"/" + str(nextDay2.day))
            lable2.grid(row= 1, column= 3,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay3.month) +"/" + str(nextDay3.day))
            lable2.grid(row= 1, column= 4,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay4.month) +"/" + str(nextDay4.day))
            lable2.grid(row= 1, column= 5,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay5.month) +"/" + str(nextDay5.day))
            lable2.grid(row= 1, column= 6,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay6.month) +"/" + str(nextDay6.day))
            lable2.grid(row= 1, column= 7,sticky= "nsew",padx= 1,pady=1)
            lable2= Label(text=str(nextDay7.month) +"/" + str(nextDay7.day))
            lable2.grid(row= 1, column= 8,sticky= "nsew",padx= 1,pady=1)
            

        elif column==0:
            a+=1
            label= Label(text=a)
            label.grid (row=row, column =column,sticky= "nsew",padx= 1,pady=1)
        else:
            user= ['John', 'Mary', 'Amy', 'Will']
            variable = StringVar(window)
            # variable.set(user[0])
            
            label6 = OptionMenu(window, variable,*user)
            label6.grid(row=row, column= column,sticky= "nsew",padx= 1,pady=1)
            window.grid_columnconfigure(column, weight= 1, uniform =1)
            
            
            
window.mainloop()
