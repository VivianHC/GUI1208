import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '240x200'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

#------------------------------
lbl_hello=tk.Label(
    top_win,
    text='Login Form',
    bg='purple',
    fg='white',
    font=('Arial',12),
    width=20,
    height=2
)
lbl_hello.place(x=2,y=2,width=20,height=2)
lbl_hello.pack()
#------------------------------


# show window and get into event loop
top_win.mainloop()
