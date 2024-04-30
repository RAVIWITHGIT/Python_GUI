# Tkinter library, the Canvas widget is a versatile tool for creating custom graphics, drawing shapes, and displaying images. Let me walk you through some basics:
# The Canvas widget is one of the available components in Tkinter that allows you to draw and manipulate graphics, such as lines, shapes, text, and images, on a rectangular area.

from tkinter import *
from PIL import Image,ImageTk

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

root.title("Ravi GUI")

# can_width = Canvas(root,width=canvas_width,height=canvas_height)
# # can_width = Canvas(root,width=600,height=200)
# can_width.pack()


# ******************************************* create line 
# the line goes from the point x1,y1 to x2,y2
# can_width.create_line(0,0,800,200)
# can_width.create_line(0,100,800,200)
# can_width.create_line(0,100,800,200)
# can_width.create_line(0,0,800,400,fill="red")
# can_width.create_line(0,400,800,0,fill="blue")

#************************************************** to create a rectangle specify parameters in this order - cooridinate of top left and coridinate of bottom right , mean cooridinate start from top left and end point bottom right
#************************************ can_width.create_rectangle(x1,y1,x2,y2,fill="blue")


# can_width.create_rectangle(0,20,100,200,fill="blue")
# can_width.create_rectangle(0,20,600,200,fill="blue")
# can_width.create_rectangle(0,20,600,0,fill="blue")
# can_width.create_rectangle(0,20,600,100,fill="blue")
# can_width.create_rectangle(0,20,600,400,fill="blue")
# can_width.create_rectangle(100,20,800,300,fill="blue")
# can_width.create_rectangle(0,20,600,400,fill="blue")


""" *****************************create Text
1.create Text help to create text in gui
2. cordinate start from center
3 we define width is 800 and height of gui is 400 , so center condinate of gui is 400x200
"""
# can_width.create_text(400,200,text="Python Gui",fill="white")
# can_width.create_text(100,200,text="Python Gui",fill="white")

"""***************************** create oval
1. oval get two cordinate --> x1,y1,x2.y2
2. top right --> x1,y1 , bottom left --> x2,y2

"""
# can_width.create_oval(100,200,300,400,fill="yellow")
# can_width.create_oval(0,0,150,200,fill="yellow")
# can_width.create_oval(800,300,0,0,fill="yellow")


"""*************************** create Image
Create_image take 3 argument 
 I. cordinate --> x,y --> 
 II. max value of x and y depande on width and height , exa - if width 800,height-400 then max value of x and y is left point (0,200) and right poing max value is (799,200)
 III. image
 IV. anchor

"""
# img = ImageTk.PhotoImage(Image.open("first.png"))
# ****can_width.create_image(x direction,y-direction,anchor=NW,image=img)
# can_width.create_image(0,100,anchor=NW,image=img)
# can_width.create_image(100,100,anchor=NW,image=img)
# can_width.create_image(200,50,anchor=NW,image=img)
# can_width.create_image(500,0,anchor=NW,image=img)

"""***************************create arh
x-coordinate of the top-left corner: 100
y-coordinate of the top-left corner: 50
x-coordinate of the bottom-right corner: 500
y-coordinate of the bottom-right corner: 300

3. start --> present in degree
4. extent --> present in degree
"""


can_width2 = Canvas(root,width=600,height=300,bg="blue")
can_width2.pack()

# coords = 100,50,500,300
# arc = can_width2.create_arc(coords,start=0,extent=150,fill="red")

# **** change cordinate
# coords = 0,50,500,300
# arc = can_width2.create_arc(coords,start=0,extent=150,fill="red")

# coords = 0,0,500,300
# arc = can_width2.create_arc(coords,start=0,extent=150,fill="red")

# coords = 0,0,200,300
# arc = can_width2.create_arc(coords,start=0,extent=150,fill="red")

# coords = 0,0,700,300
# arc = can_width2.create_arc(coords,start=0,extent=150,fill="red")


# **** change extent

# arc = can_width2.create_arc(coords,start=0,extent=100,fill="red")
# arc = can_width2.create_arc(coords,start=0,extent=50,fill="red")
# arc = can_width2.create_arc(coords,start=0,extent=10,fill="red")
# arc = can_width2.create_arc(coords,start=0,extent=300,fill="red")

# **** change start
# arc = can_width2.create_arc(coords,start=0,extent=90,fill="red")
# arc = can_width2.create_arc(coords,start=40,extent=90,fill="red")
# arc = can_width2.create_arc(coords,start=10,extent=150,fill="red")
# arc = can_width2.create_arc(coords,start=50,extent=150,fill="red")



root.mainloop()