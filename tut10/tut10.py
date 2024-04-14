from tkinter import *

"""Get Input value , we use get() method


"""
def showvalue():
    print(userValue.get())
    print(passValue.get())

root = Tk()
root.geometry("666x333")

""" grid take two parammeter 
1. first--> row
2. second --> column
3. syntex is --> grid(row=0,column=0)

4. bydiffult row is 0 and column is 0
"""


user = Label(root,text="User Name")
password = Label(root,text="Enter Password")
user.grid(row=0)
password.grid(row=1)


"""varaible class in tkinter
BooleanVar,DoubleVar,IntVar,StringVar

"""

userValue = StringVar()
passValue = StringVar()


"""creat Input Fild using Entry() function

"""
userEntry = Entry(root,textvariable=userValue)
passEntry = Entry(root,textvariable=passValue)
userEntry.grid(row=0,column=1)
passEntry.grid(row=1,column=1)
mybotton = Button(text="submit",command=showvalue)
mybotton.grid()

root.mainloop()