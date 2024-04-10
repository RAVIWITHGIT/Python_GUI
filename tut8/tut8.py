"""
this tutorial discuss about Frame. Frame like a section mean when make website then we use multiple section for diffrent part , same Frame like a section which part of window screen

"""


from tkinter import *
root = Tk()
root.geometry("655x333")
root.minsize(655,333)
f1 = Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l1 = Label(f1,text="project Tkiner - Vscode",fg="black",bg="pink")
l1.pack(pady=142)
l2 = Label(f2,text="welcome the vscode GUI",font="Helvetica 16 bold",fg="white",bg="grey")
l2.pack()

root.mainloop()