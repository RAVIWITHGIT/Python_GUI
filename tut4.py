# here we discuss about important lable option 


from tkinter import *

root = Tk()
root.geometry("744x300")
root.title("my GUI with Harry")

""" ********************************************************** important Lable Options
1. text --> adds the text
2. bd/background --> for background color
3. fg/foreground  --> change text color
4. font --> set the font , we can set font two way
  I. font=("fontName",fontSize,"fontWeight") --> here we define diffrent diffrent double code 
  II. font="fontName fontSize fontWeight"   --> all write in one double code
5. padx --> x padding
6. pady --> y padding
7. relief --> border styling (SUNKEN,PAISED,GROOVE,RIDGE)  

"""

title_lable = Label(text='''Hinduism [1][2] is an Indian religion or dharma, a religious and universal order or way of life by which followers\n abide.[note 1][note 2] The word Hindu is an exonym,[note 3] and while Hinduism has been called\n usage, based on the belief that its origins lie beyond human history, as revealed in the Hindu texts.\n[note 5] Another endonym for Hinduism is Vaidika dharma.[web 1]Hinduism entails diverse systems of \nthought, marked by a range of shared concepts that discuss theology, mythology, among other topics, \nin textual sources.[3] The major Hindu denominations are Vaishnavism, Shaivism, Shaktism, and the \nSmarta tradition. The six Āstika schools of Hindu philosophy, which recognise the authority of the \nVedas, are: Sānkhya, Yoga, Nyāya, Vaisheshika, Mimāmsā, and Vedānta.[4][5] Hindu texts have been \n ''',bg="green",fg="white",padx=20,pady=94,font="comicsansms 9 bold", borderwidth=9,relief=SUNKEN)



""" ********************************************************** important pack  Options
1. anchor --> mean direction = nw(north-west),se(south-east) etc.
2. side --> top, right,bottom, left  (bydiffult is top)
3. fill ---> adapt/fullfill the space x and y direction
4. paddx --> padding x direction
5. paddy --> padding y direction
"""


# ------------anchor

# title_lable.pack(anchor="nw")

# ----------- side with anchor
# title_lable.pack(side="bottom")
# title_lable.pack(side="bottom",anchor="nw")

# ---------- side,anchor,fill

# ** without fill
# title_lable.pack(anchor="nw",side="bottom")

# ** with fill
# title_lable.pack(anchor="nw",side="bottom",fill=X)

# ** for y direction fill side is left or rigth
# title_lable.pack(anchor="nw",side="left",fill=Y)

# --------- side,anchor,fill,padding

# --- without padding
# title_lable.pack(anchor="nw",fill=X)
# --- with padding
# title_lable.pack(anchor="nw",fill=X,padx=100)
title_lable.pack(anchor="sw",fill=X,pady=50)






root.mainloop()