# python file

from tkinter import *
from PIL import ImageTk,Image

root = Tk()

def every_100(text):
    mytext = ""
    for i in range(0,len(text)):
        mytext +=text[i]
        if i%90==0 and i!=0:
            mytext +="\n"
    return mytext

root.geometry("666x650")
root.title("RAVI NEWS-PAPER")

mytext = []
myphoto = []

for i in range(0,3):
    with open(f"{i+1}.txt","r",encoding="utf-8") as f:
        text = f.read()
        mytext.append(every_100(text))

    image = Image.open(f"{i+1}.png")   
    image = image.resize((225,200),Image.Resampling.LANCZOS)
    myphoto.append(ImageTk.PhotoImage(image))

fo = Frame(root,width=400,height=100)
Label(fo,text="Daly News Updates",font="lucide 25 bold",bg="green",fg="blue",highlightbackground = "black",highlightthickness = 4, bd=0).pack()
fo.pack()
Label(fo,text="5/7/2024",font="lucide 13 bold",pady=16).pack()
fo.pack()

f1 = Frame(root,width=400,height=100)
Label(f1,text=mytext[0]).pack(side="left")
Label(f1,image=myphoto[0]).pack()
f1.pack()

f2 = Frame(root,width=400,height=100)
Label(f2,text=mytext[1]).pack(side="right")
Label(f2,image=myphoto[1]).pack()
f2.pack()

f3 = Frame(root,width=400,height=100)
Label(f3,text=mytext[2]).pack(side="left")
Label(f3,image=myphoto[2]).pack()
f3.pack()




        

root.mainloop()