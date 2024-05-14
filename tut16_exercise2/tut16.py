from tkinter import *

root = Tk()

mwidth = '656'
mheight = '344'

def getvalue():
    root.geometry(f'{NewwidthSize.get()}x{NewHeightSize.get()}')

    

root.geometry(f'{mwidth}x{mheight}')

widthtext = Label(root,text="write new width")
widthtext.grid(row=0)
heighttext = Label(root,text="write new height")
heighttext.grid(row=1)

NewwidthSize =StringVar() 
NewHeightSize =StringVar() 

widthEntry = Entry(root,textvariable=NewwidthSize)
widthEntry.grid(row=0,column=1)
heightEntry = Entry(root,textvariable=NewHeightSize)
heightEntry.grid(row=1,column=1)

mybutton = Button(text="submit" ,command=getvalue)
mybutton.grid()


root.mainloop()