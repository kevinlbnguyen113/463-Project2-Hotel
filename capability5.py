from tkinter import *
from PIL import Image, ImageTk


def full_dimensions(img):
    top = Toplevel(window)
    pic = Label(top, image=img)
    pic.pack()


window = Tk()
width = 400
height = 950
window.title('Guest Information')
window.geometry('400x950')
window.resizable(False, False)
label_frame = Frame(window, width=width, height=height, bg='white')
image1 = Image.open('icon.jpg').resize((200, 100), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
image2 = image1.resize((600, 400), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
photo = Button(label_frame, image=photo1, command=lambda: full_dimensions(photo2)).place(x=100, y=20)
first_name_label = Label(label_frame, text='First Name', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=160)
first_name_text = Label(label_frame, text='Henry', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=200)
last_name_label = Label(label_frame, text='First Name', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=260)
last_name_text = Label(label_frame, text='Mo', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=300)
phone_number_label = Label(label_frame, text='Phone Number', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=360)
phone_number_text = Label(label_frame, text='(123)456-7890', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=400)
address_label = Label(label_frame, text='Address', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=460)
address_text1 = Label(label_frame, text='123 This Ave.', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=500)
address_text2 = Label(label_frame, text='ThatCity, CA 12345', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=540)
email_address_label = Label(label_frame, text='Email Address', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=600)
email_address_text = Label(label_frame, text='testing@gmail.com', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=640)
id_label_label = Label(label_frame, text='ID info', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=700)
id_label_text = Label(label_frame, text='123456789', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=740)
vehicle_license_plate_label = Label(label_frame, text='Vehicle License Plate', bg='white', fg='light gray', font=('Arial', 16)).place(x=80, y=800)
vehicle_license_plate_text = Label(label_frame, text='123456789', bg='white', fg='black', font=('Arial', 16)).place(x=80, y=840)
label_frame.place(x=0, y=0)
window.mainloop()
