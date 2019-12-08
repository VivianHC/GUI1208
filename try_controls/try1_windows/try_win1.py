
import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '1920x1080'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

#------------------------------

#------------------------------


# show window and get into event loop
top_win.mainloop()
