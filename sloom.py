from tkinter import *
import vlc
import sys
import os
import time
from pypresence import Presence

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

rpc = Presence("914268050583343124")
rpc.connect()
rpc.update(state="sloom",details="Slooming",large_image="sloom",start=time.time())


root = Tk()
root.title('Sloom')
HEIGHT = 100
WIDTH = 100
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
image = PhotoImage(file=r"sloom.png")
canvas.create_image(WIDTH/2, HEIGHT/2, anchor="center", image=image)
root.resizable(width=False, height=False)
canvas.pack()

player = vlc.Instance()

p = vlc.MediaPlayer("Sloom.mp3")
p.play()


root.mainloop()