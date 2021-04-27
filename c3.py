import tkinter as tk

def buttonClick():
    dailyRate_label = tk.Label(labelFrame, text="Daily Rate: Placeholder")
    dailyRate_label.pack()
    totalCharge_label = tk.Label(labelFrame, text="Total Charge: Placeholder")
    totalCharge_label.pack()

def reservationClick():
    newWindow = tk.Toplevel(labelFrame, width=540, height=310)
    firstNameR_label = tk.Label(newWindow, text="First Name")
    firstNameR_label.pack()

    lastNameR_label = tk.Label(newWindow, text="Last Name")
    lastNameR_label.pack()

    dateCheckInR_label = tk.Label(newWindow, text="Date Check-In")
    dateCheckInR_label.pack()

    dateCheckOutR_label = tk.Label(newWindow, text="Date Check Out")
    dateCheckOutR_label.pack()

    RoomTypeR_label = tk.Label(newWindow, text="Room Type")
    RoomTypeR_label.pack()

    RateR_label = tk.Label(newWindow, text="Rate")
    RateR_label.pack()

    totalChargeR_label = tk.Label(newWindow, text="Total Charge")
    totalChargeR_label.pack()

window = tk.Tk()
width = 640
height = 480
window.title('Reservations')
window.geometry('640x480')
window.resizable(True, True)
labelFrame = tk.Frame(window, width=width, height=height)


roomTypes = [
    "King(K)",
    "Double Queen(DQ)",
    "Double Queen with Kitchen(DQK)",
    "Suite(S)"
]

firstName_label = tk.Label(labelFrame, text="First Name")
firstName_entry = tk.Entry()
firstName_label.pack(), firstName_entry.pack()

lastName_label = tk.Label(labelFrame, text="Last Name")
lastName_entry = tk.Entry()
lastName_label.pack(), lastName_entry.pack()

dateCheckIn_label = tk.Label(labelFrame, text="Date Check-In")
dateCheckIn_entry = tk.Entry()
dateCheckIn_label.pack(), dateCheckIn_entry.pack()

dateCheckOut_label = tk.Label(labelFrame, text="Date Check Out")
dateCheckOut_entry = tk.Entry()
dateCheckOut_label.pack(), dateCheckOut_entry.pack()

dropdown_label = tk.Label(labelFrame, text="Room Type")
dropdownClicked = tk.StringVar()
dropdownClicked.set("Select room type")
dropdown = tk.OptionMenu(window, dropdownClicked, *roomTypes)
dropdown.pack()

# for now, don't check if available, activate fields for daily rate and total charge regardless
checkAvailabilityBtn = tk.Button(window, command=buttonClick, text="Check Availability")
checkAvailabilityBtn.place(x=265, y=390)

showReservationsBtn = tk.Button(window, command=reservationClick, text="Show Reservations")
showReservationsBtn.place(x=265, y=410)

labelFrame.place(x=0, y=0)
window.mainloop()


