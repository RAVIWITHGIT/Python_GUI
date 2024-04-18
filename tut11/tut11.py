from tkinter import *

def submitvalue():
    print(namevalue.get())
    print(phonevalue.get())
    print(gendervalue.get())
    print(emergencyvalue.get())
    print(paymentModevalue.get())
    print(foodServicevalue.get())

root = Tk()

root.geometry("666x333")
Label(root,text="welcome to my page",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)



name = Label(root,text="name")
phone = Label(root,text="phone")
gender = Label(root,text="gender")
emergency = Label(root,text="emergency")
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
foodServicevalue = IntVar()

nameEntery = Entry(root,textvariable=namevalue)
phoneEntery = Entry(root,textvariable=phonevalue)
genderEntery = Entry(root,textvariable=gendervalue)
emergencyEntery = Entry(root,textvariable=emergencyvalue)
paymentModeEntery = Entry(root,textvariable=paymentModevalue)

nameEntery.grid(row=1,column=1)
phoneEntery.grid(row=2,column=1)
genderEntery.grid(row=3,column=1)
emergencyEntery.grid(row=4,column=1)
paymentModeEntery.grid(row=5,column=1)

foodService = Checkbutton(text="want foodServide or not",variable=foodServicevalue)
foodService.grid(row=6,column=1)

Button(text="submit form",command=submitvalue).grid(row=7,column=1)

root.mainloop()