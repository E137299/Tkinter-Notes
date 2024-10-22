from tkinter import *
import random

root = Tk()
root.title("Tkinter Demo")
root.geometry("800x600+40+40")

### MODEL ###
def change_title():
    title_text = ["T","k","i","n","t","e","r"," ","D","e","m","o"]
    random.shuffle(title_text)
    title_text = "".join(title_text)
    
    title.config( text = title_text, bg = random.choice(["red","green","blue"]))

def frame_changer(frame):
    frame.tkraise()


frame2 = Frame(root, bg = "red" )
frame2.place(x=0,y=0, width = 800, height = 600)

frame1 = Frame(root, bg = "blue" )
frame1.place(x=0,y=0, width = 800, height = 600)


### CONTROLLER ###
button1 = Button(frame1, bg = "#A1EEFF", fg = "#333300", text="Press Me to Change Title", command = change_title )
button1.place(x = 300, y = 100, width = 200, height = 50)

button2 = Button(frame1, bg = "#A1EEFF", fg = "#333300", text="Press Me to Frame", command = lambda: frame_changer(frame2) )
button2.place(x = 300, y = 200, width = 200, height = 50)

button3 = Button(frame2, bg = "#A1EEFF", fg = "#333300", text="Press Me to Frame", command = lambda: frame_changer(frame1) )
button3.place(x = 300, y = 200, width = 200, height = 50)

### VIEW ###
title = Label(frame1, bg = "blue", fg = "white", text = "Tkinter Demo", font = ("Times New Roman",24))
title.place(x = 300, y = 20, width = 200, height = 50)






root.mainloop()