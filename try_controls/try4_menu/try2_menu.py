import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

#------------------------------
# create a top menu
top_menu = tk.Menu(top_win)
top_menu.add_command(label="Hello", command=None)
top_menu.add_command(label="Quit", command=top_win.quit)

# show the menu
top_win.config(menu=top_menu)

#------------------------------


# show window and get into event loop
top_win.mainloop()
