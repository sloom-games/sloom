#Imports
from tkinter import *
import tkinter as tk
import sys
import os
import time
import datetime


#Variables
root = tk.Tk()
root.title('Sloom')
root.iconbitmap('sloom.ico')
root.resizable(width=False, height=False)
height = 300
width = 300

#Time Wasted
def time_elapsed():
    session = str(datetime.timedelta(seconds=int(round(time.time()-elapsed))))
    timer.config(text=session)
    timer.after(200, time_elapsed)

global elapsed
elapsed = time.time()

#SLOOM IMAGE !
image = PhotoImage(file=r"sloom.png")
canvas = Canvas(root, height=height, width=width)
canvas.create_image(width/2, height/2, anchor="center", image=image)
canvas.pack()

#Time Wasted Text
time_wasted = Label(root, text="Time Wasted", font=("Comic Sans MS", 15, "bold"))
time_wasted.pack()

#Timer
timer = Label(root, font=("Comic Sans MS", 20))
timer.pack()
time_elapsed()

#this
root.mainloop()
