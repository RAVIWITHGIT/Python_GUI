from tkinter import *

main_root = Tk()


# UI kes size mein dikhega vah ham geometry method ki andar likhate hai, Width X Height
main_root.geometry("733x434")

# minimum size
main_root.minsize(200,100)

# maxsize
main_root.maxsize(1000,500)

# create a lable
mylable = Label(text="This UI Create By Ravi")
mylable.pack()

main_root.mainloop()