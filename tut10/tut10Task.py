# f.write("hello ravi how are you\n")
# f.write("hello ravi how are you")
# f.write("hello ravi how are you")
# f.close()
from tkinter import *


def showvalue():
    f = open("storeData.txt","a")
    f.write(f"Name is {NameValue.get()}\n")
    f.write(f"age is {ageValue.get()}\n")
    f.write(f"dance type is {DanceValue.get()} \n")
    f.write(f"music  is {MusicValue.get()} \n")
    
    f.close()    
    
    print("submit form")
    
root = Tk()

root.geometry("666x333")

userName = Label(root,text="enter your name")
userAge = Label(root,text="Enter your age")
DanceType = Label(root,text="single/Couple")
MusicType = Label(root,text="entery what type of music you like")

userName.grid()
userAge.grid()
DanceType.grid()
MusicType.grid()

NameValue =StringVar()
ageValue =StringVar()
DanceValue =StringVar()
MusicValue =StringVar()

NameEntry = Entry(root,textvariable=NameValue)
ageEntry = Entry(root,textvariable=ageValue)
danceEntry = Entry(root,textvariable=DanceValue)
musicEntry = Entry(root,textvariable=MusicValue)

NameEntry.grid(row=0,column=1)
ageEntry.grid(row=1,column=1)
danceEntry.grid(row=2,column=1)
musicEntry.grid(row=3,column=1)

submitButton = Button(text="submit",command=showvalue)
submitButton.grid()

root.mainloop()