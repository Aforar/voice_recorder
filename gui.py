import tkinter as tk
from tkinter import *


def screen_record_voice():
    root = tk.Tk()
    #this line for screen of software 1000x700.
    root.geometry("%dx%d" % (1000, 700))

    Label_Time = tk.Label(root,
                          text= "00:00:00",
                          font=("Arial",30),)
    Label_Time.place(relx=0.5, rely=0.0, anchor="n")




    root.mainloop()