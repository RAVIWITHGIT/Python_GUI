"""
here we discuss how make menu section
"""


from tkinter import *

root = Tk()
root.geometry('333x340')

def clickmenu():
    print("click on file menu")

#**************** basic menu wihout dropdown
# mymenu = Menu(root)
# mymenu.add_command(label="file", command=clickmenu)
# mymenu.add_command(label="quit", command=quit)
# root.config(menu=mymenu)

# ***************menu with dropdown/summenu
"""
when we open submenu then first line see like ------, this is called tearoff . which is used seprately from main manu and submenu
"""

# mainmenu = Menu(root)

# m1 = Menu(mainmenu)
# m1.add_command(label="New Text file")
# m1.add_command(label="New file")
# m1.add_command(label="New window")
# mainmenu.add_cascade(label="file",menu=m1)



# m2 = Menu(mainmenu)
# m2.add_command(label="New Text file")
# m2.add_command(label="New file")
# m2.add_command(label="New window")

# mainmenu.add_cascade(label="Edit",menu=m2)


# root.config(menu=mainmenu)


"""
****************hide tearoff

"""

# mainmenu = Menu(root)
# m1 = Menu(mainmenu,tearoff=0)
# m1.add_command(label="add new file")
# m1.add_command(label="add  file")
# m1.add_command(label="add new window")
# mainmenu.add_cascade(label="File",menu=m1)
# root.config(menu=mainmenu)



"""
**************** seprate submenu label

"""

# mainmenu = Menu(root)
# m1 = Menu(mainmenu,tearoff=0)
# m1.add_command(label="add new file")
# m1.add_command(label="add  file")
# m1.add_command(label="add new window")
# m1.add_separator()
# m1.add_command(label="open file")
# m1.add_command(label="open folder")
# mainmenu.add_cascade(label="File",menu=m1)

# m2 = Menu(mainmenu,tearoff=0)
# m2.add_command(label="add new file")
# m2.add_command(label="add  file")
# m2.add_command(label="add new window")
# m2.add_separator()
# m2.add_command(label="cut")
# m2.add_command(label="copy")
# m2.add_command(label="past")
# mainmenu.add_cascade(label="Edit",menu=m2)


# root.config(menu=mainmenu)



root.mainloop()