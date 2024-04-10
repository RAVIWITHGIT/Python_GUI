from tkinter import *
from PIL import Image , ImageTk


root = Tk()
root.geometry("700x300")


image = Image.open("1.jpeg")
resize_img = image.resize((300,200))
photo = ImageTk.PhotoImage(resize_img)
photo_var = Label(image=photo)

image2 = Image.open("2.jpeg")
resize_img2 = image2.resize((300,200))
photo2 = ImageTk.PhotoImage(resize_img2)
photo_var2 = Label(image=photo2)

image3 = Image.open("3.jpeg")
resize_img3 = image3.resize((300,200))
photo3 = ImageTk.PhotoImage(resize_img3)
photo_var3 = Label(image=photo3)

image4 = Image.open("4.jpeg")
resize_img4 = image4.resize((300,200))
photo4 = ImageTk.PhotoImage(resize_img4)
photo_var4 = Label(image=photo4)

image5 = Image.open("5.jpeg")
resize_img5 = image5.resize((300,200))
photo5 = ImageTk.PhotoImage(resize_img5)
photo_var5 = Label(image=photo5)



text_lable = Label(root,text='''
Locally nicknamed "La dame de fer" (French for "Iron Lady"), it was constructed as the centerpiece\n of the 1889 World's Fair, and to crown the centennial anniversary of the French Revolution. Although \ninitially criticised by some of France's leading artists and intellectuals for its design, it has \nsince become a global cultural icon of France and one of the most recognisable structures in the \nworld.[5] The tower received 5,889,000 visitors in 2022.[6] The Eiffel Tower is the most visited \nmonument with an entrance fee in the world:[7] 6.91 million people ascended it in 2015. It was \ndesignated a monument historique in 1964, and was named part of a UNESCO World Heritage Site \n("Paris, Banks of the Seine") in 1991.[8]
''')
# text_lable2 = Label(root,text="hello ravi")
# text_lable3 = Label(root,text="hello ravi")
# text_lable4 = Label(root,text="hello ravi")
# text_lable5 = Label(root,text="hello ravi")

photo_var.grid(row=0,column=0)
photo_var2.grid(row=1,column=0)
photo_var3.grid(row=2,column=0)
photo_var4.grid(row=3,column=0)
photo_var5.grid(row=4,column=0)

text_lable.grid(row=0,column=1)

root.mainloop()

# ----------------------------------------

# from tkinter import *

# root = Tk() 
# root.geometry("150x200") 

# w = Label(root, text ='GeeksForGeeks', 
# 		font = "50") 

# w.pack() 

# scroll_bar = Scrollbar(root) 

# scroll_bar.pack( side = RIGHT, 
# 				fill = Y ) 

# mylist = Listbox(root, 
# 				yscrollcommand = scroll_bar.set ) 

# image = Image.open("1.jpeg")
# resize_img = image.resize((300,200))
# photo = ImageTk.PhotoImage(resize_img)
# photo_var = Label(image=photo)

# for line in range(1, 100): 
# 	mylist.insert(END, photo_var + str(line)) 

# mylist.pack( side = LEFT, fill = BOTH ) 

# scroll_bar.config( command = mylist.yview ) 

# root.mainloop() 
