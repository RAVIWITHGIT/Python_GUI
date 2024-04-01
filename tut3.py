from tkinter import *
from PIL import Image , ImageTk
import os

main_root = Tk()

main_root.geometry("800x890")

#--------------------------------------- use png image
# photo = PhotoImage(file="pngwing.com.png")
# photo_var = Label(image=photo)
# photo_var.pack()




#  tkinter support only png image , if you want support jpg  type of image  then
# first - install --> pip install pillow
# second - use this code
# image = Image.open("unnamed.jpg")
# photo = ImageTk.PhotoImage(image)
# photo_var = Label(image=photo)
# photo_var.pack()



""" -------------------------------------------------------------------
if use avif image

1. first install --> pip install pillow pillow-avif-plugin --upgrade
2. second --> use this code
"""

# from tkinter import *
# from PIL import Image , ImageTk
# import pillow_avif  # Have to import this before importing PIL
# from PIL import Image
# main_root = Tk()
# main_root.geometry("800x890")

# image = Image.open("first.avif")

# photo = ImageTk.PhotoImage(image)
# photo_var = Label(image=photo)
# photo_var.pack()



# --------------------------------------------- show multiple image
# mylable.pack()

# image1 = Image.open("pngwing.com.png")
# image1 = image1.resize((240, 240))
# image1 = ImageTk.PhotoImage(image1)

# image2 = Image.open("unnamed.jpg")
# image2 = image2.resize((240, 240))
# image2 = ImageTk.PhotoImage(image2)

# image3 = Image.open("unnamed.jpg")
# image3 = image3.resize((240, 240))
# image3 = ImageTk.PhotoImage(image3)

# image4 = Image.open("unnamed.jpg")
# image4 = image4.resize((240, 240))
# image4 = ImageTk.PhotoImage(image4)


# label1 = Label(image=image1)
# label2 = Label(image=image2)
# label3 = Label(image=image3)
# label4 = Label(image=image4)

# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1)
# label3.grid(row=1, column=0)
# label4.grid(row=1, column=1)



# -----------------------------------------------------
folder = os.listdir("img")


image1 = Image.open(folder[0])
image1 = image1.resize((240, 240))
image1 = ImageTk.PhotoImage(image1)

image2 = Image.open(folder[1])
image2 = image2.resize((240, 240))
image2 = ImageTk.PhotoImage(image2)



label1 = Label(image=image1)
label2 = Label(image=image2)


label1.grid(row=0, column=0)
label2.grid(row=0, column=1)



main_root.mainloop()
