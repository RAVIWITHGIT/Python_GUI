from tkinter import *

def submitform():
    print(f" {namevalue.get()} {phonevalue.get()} {gendervalue.get()} {emergencyvalue.get()} {paymentModevalue.get()} {servicevalue.get()}")
    with open("record.txt","a") as f:
        f.write(f" {namevalue.get()} {phonevalue.get()} {gendervalue.get()} {emergencyvalue.get()} {paymentModevalue.get()} {servicevalue.get()} \n")

root = Tk()

root.geometry("666x333")
Label(root,text="welcome to my Form", pady=15).grid(row=0,column=3)

name = Label(root,text="name")
phone = Label(root,text="phone")
gender = Label(root,text="gender")
emergency =  Label(root,text="emergency")
paymentMode = Label(root,text="paymentMode")

name.grid(row=1,column=0)
phone.grid(row=2,column=0)
gender.grid(row=3,column=0)
emergency.grid(row=4,column=0)
paymentMode.grid(row=5,column=0)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentModevalue = StringVar()
servicevalue = IntVar()

nameEntry = Entry(root,textvariable=namevalue)
phoneEntry = Entry(root,textvariable=phonevalue)
genderEntry = Entry(root,textvariable=gendervalue)
emergencyEntry = Entry(root,textvariable=emergencyvalue)
paymentModeEntry = Entry(root,textvariable=paymentModevalue)

nameEntry.grid(row=1,column=1)
phoneEntry.grid(row=2,column=1)
genderEntry.grid(row=3,column=1)
emergencyEntry.grid(row=4,column=1)
paymentModeEntry.grid(row=5,column=1)

foodService = Checkbutton(text="want foodServide or not",variable=servicevalue)
foodService.grid(row=6,column=1)
Button(text="submit form",command=submitform).grid(row=7,column=1)

root.mainloop()