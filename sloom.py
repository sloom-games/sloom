#Imports
from tkinter import *
import tkinter as tk
import pygame
import sys
import os
import time
from pypresence import Presence
import datetime

#Pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Variables
root = tk.Tk()
root.title('Sloom')
root.iconbitmap('sloom.ico')
root.resizable(width=False, height=False)
height = 300
width = 300

global elapsed
elapsed = time.time()

#Time Elapsed
def time_elapsed():
    session = str(datetime.timedelta(seconds=int(round(time.time()-elapsed))))
    timer.config(text=session)
    timer.after(200, time_elapsed)

#Sloom Music
pygame.mixer.init()
def sloom_music():
    pygame.mixer.music.load("Sloom.mp3")
    pygame.mixer.music.play(loops=0)

#Discord Presence
#if discord is not open it wont crash the program
try:
    rpc = Presence("914268050583343124")
    rpc.connect()
    rpc.update(state="sloom", details="Slooming", large_image="sloom", start=time.time())
except:
    print("Discord not found")
    discord = Label(root, text="Discord not found", fg='red')
    discord.pack()

#Sloom
sloom_music()

#UI
sloom = Label(root, text="Sloom", font=("Comic Sans MS", 35, "bold"))
sloom.pack()

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