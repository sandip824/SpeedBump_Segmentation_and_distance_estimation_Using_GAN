from tkinter import *
from tkinter import messagebox
import numpy as np
import os
#import pickle
import time

def clicked4m():
    os.system('/home/pi/webcam/./4m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked6m():
    os.system('/home/pi/webcam/./6m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked8m():
    os.system('/home/pi/webcam/./8m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked10m():
    os.system('/home/pi/webcam/./10m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked12m():
    os.system('/home/pi/webcam/./12m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked14m():
    os.system('/home/pi/webcam/./14m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked16m():
    os.system('/home/pi/webcam/./16m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked18m():
    os.system('/home/pi/webcam/./18m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def clicked20m():
    os.system('/home/pi/webcam/./20m.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def capturerandom():
    os.system('/home/pi/webcam/./random.sh')
    #messagebox.showinfo('Data Saved', 'Successfully saved image to selected folder ')
def close_window():
    res = messagebox.askyesno('exit', 'Are you sure you want to exit')
    if res == TRUE:
        window.destroy()


window = Tk()
window.title("Speed Bump Data Collector")
window.geometry('720x270')
window.configure(bg='#D5F5E3')
lbl = Label(window, text="Click on the button to save image to known distance folder",bg="orange")
lbl.grid(column=3, row=0)

seconds = Entry(window, width=10)
seconds.grid(column=4, row=7)

btn = Button(window, text="Bump@4m", command=clicked4m, bg="#2874A6", fg="white")
btn.grid(column=2, row=2)
btn = Button(window, text="Bump@6m", command=clicked6m, bg="#2874A6", fg="white")
btn.grid(column=3, row=2)
btn = Button(window, text="Bump@8m", command=clicked8m, bg="#2874A6", fg="white")
btn.grid(column=4, row=2)
btn = Button(window, text="")
btn.grid(column=3, row=3)
btn = Button(window, text="Bump@10m", command=clicked10m, bg="#2874A6", fg="white")
btn.grid(column=2, row=4)
btn = Button(window, text="Bump@12m", command=clicked12m, bg="#2874A6", fg="white")
btn.grid(column=3, row=4)
btn = Button(window, text="Bump@14m", command=clicked14m, bg="#2874A6", fg="white")
btn.grid(column=4, row=4)
btn = Button(window, text="")
btn.grid(column=3, row=5)
btn = Button(window, text="Bump@16m", command=clicked16m, bg="#2874A6", fg="white")
btn.grid(column=2, row=6)
btn = Button(window, text="Bump@18m", command=clicked18m, bg="#2874A6", fg="white")
btn.grid(column=3, row=6)
btn = Button(window, text="Bump@20m", command=clicked20m, bg="#2874A6", fg="white")
btn.grid(column=4, row=6)


btn = Button(window, text="")
btn.grid(column=3, row=7)

btn = Button(window, text="CaptureRandom", command=capturerandom, bg="#008080", fg="black")
btn.grid(column=3, row=8)
btn = Button(window, text="RecordVideo", command=clicked20m, bg="#008080", fg="black")
btn.grid(column=4, row=8)

btn = Button(window, text="Exit", command=close_window, bg="#008080", fg="red")
btn.grid(column=3, row=9)

window.mainloop()