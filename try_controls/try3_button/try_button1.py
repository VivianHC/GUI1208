import tkinter.messagebox

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
def cmd_print():
    print('Show in command window...')
    return

def cmd_pop():
    tk.messagebox.showinfo(title='Information',
                            message='Mouse clicked!')

    tk.messagebox.showwarning(title='Warning',
                            message='Mouse clicked!')

    tk.messagebox.showerror(title='Error',
                            message='Mouse clicked!')
    return
btn_help=tk.Button(top_win,text='Push me!',command=cmd_pop)
btn_help.pack()

#------------------------------


# show window and get into event loop
top_win.mainloop()
