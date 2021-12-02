#Imports
from tkinter import *
import tkinter as tk
import pygame
import sys
import os
import time
from pypresence import Presence

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

pygame.mixer.init()
def sloom_music():
    pygame.mixer.music.load("Sloom.mp3")
    pygame.mixer.music.play(loops=1)

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
sloom = Label(root, text="Sloom", font=("Comic Sans MS", 16))
sloom.pack()

image = PhotoImage(file=r"sloom.png")
canvas = Canvas(root, height=height, width=width)
canvas.create_image(width/2, height/2, anchor="center", image=image)
canvas.pack()

#this
root.mainloop()