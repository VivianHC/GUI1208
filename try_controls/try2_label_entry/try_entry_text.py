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
default_var=tk.StringVar(value='一人之下')
txt_desc=tk.Text(top_win,height=6,width=100)
txt_desc.pack()

ent_row=tk.Entry(
    top_win,
    show=None,
    textvariable=default_var,
)
ent_row.place(x=100,y=100,width=150)
#------------------------------


# show window and get into event loop
top_win.mainloop()
