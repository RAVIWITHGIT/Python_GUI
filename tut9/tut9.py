from tkinter import *

root = Tk()

root.geometry("655x333")

def ffun():
    print("print first function")
def sfun():
    print("print second function")
def tfun():
    print("print third function")
def fofun():
    print("print four function")

frame = Frame(root,borderwidth=6,bg="grey")
frame.pack(side="left",anchor="nw")

b1 = Button(frame,fg="red",text="first button",command=ffun)
b1.pack(side=LEFT)
b2 = Button(frame,fg="red",text="second button",command=sfun)
b2.pack(side=LEFT)
b3 = Button(frame,fg="red",text="third button",command=tfun)
b3.pack(side=LEFT)
b4 = Button(frame,fg="red",text="four button",command=fofun)
b4.pack(side=LEFT)

root.mainloop()