"""
1.this tutorial we discuss how make message box
2. import tkinter.messagebox as tmasg for show message box


"""


from tkinter import *
import tkinter.messagebox as tmasg
root = Tk()

root.geometry('666x340')

def showsomething():
    print("click the help button")
    tmasg.showinfo("help","Ravi will help you with this gui")

def rate():
    value = tmasg.askquestion("was your experience good?","you use this gui... Was your experience good?")
    # print(value)
    if value=="yes":
        msg = "Great. Rate us On appstore please"
    else:
        msg = "Tell us what went wrong. we will call you soon"   
    tmasg.showinfo("Experience",msg)     

def sure():
    a = tmasg.askretrycancel("Play again",'Are you sure want to Play again')
    if(a):
        tmasg.showerror("error","some error")
        
    print(a)
    
def delete():
    tmasg.showwarning("Delete ","Are you Sure Want to delete")

def back():
    tmasg.askokcancel("back","want to back")    

Mainmenu = Menu(root)
file = Menu(Mainmenu,tearoff=0)
file.add_command(label="New Text file")
file.add_command(label="New file")
file.add_command(label="New Window")
file.add_separator()
file.add_command(label="opne file")
file.add_command(label="opne folder")
Mainmenu.add_cascade(label="file",menu=file)

Edit = Menu(Mainmenu,tearoff=0)
Edit.add_command(label="Undo")
Edit.add_command(label="Redo")
Edit.add_separator()
Edit.add_command(label="cut")
Edit.add_command(label="copy")
Edit.add_command(label="past")
Mainmenu.add_cascade(label="Edit",menu=Edit)

Help = Menu(Mainmenu,tearoff=0)
Help.add_command(label="Help", command=showsomething)
Help.add_command(label="Rate", command=rate)
Help.add_command(label="Retry", command=sure)
Help.add_command(label="Delete", command=delete)
Help.add_command(label="Back", command=back)
Mainmenu.add_cascade(label="Help",menu=Help)


root.config(menu=Mainmenu)

root.mainloop()
