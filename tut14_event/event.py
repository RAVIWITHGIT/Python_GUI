"""********************************Here we discuss about Event 
1. Many type event present in tkinter
<Button-1> --> when one click on button
<Double-Button-1> --> when double click on button

2. more event read in future
"""

from tkinter import *

# *** when we add function on click eventlistner and not give argument then give error
# def clickfun():
#     print("click the button")

# ******* then give arguments
def clickfun(event):
    # print("click the button")
    print(f"click the button {event.x} {event.y}")

root = Tk()

root.title("Event")
root.geometry("600x335")

widgth = Button(root,text="click me please")
widgth.pack()

widgth.bind('<Button-1>',clickfun)
widgth.bind('<Double-1>',quit)

root.mainloop()

