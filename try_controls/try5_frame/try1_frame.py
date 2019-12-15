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
# Step1: Create frame
frame_root1 = tk.Frame(top_win, bg="#BF3EFF", width=760, height=200)
# frame_root1.pack()
frame_root1.place(x=20, y=20)
# Step2: Appedn other controls
lbl_test = tk.Label(frame_root1, text='text in frame')
lbl_test.place(x=0, y=0)
# Step2: Appedn other controls
lbl_test2 = tk.Label(top_win, text='text TOP WIN')
lbl_test2.place(x=20, y=200)

def cmd_undo():
    tk.messagebox.showinfo(title='Info', message='Undo sth.')  # 提示信息对话窗
    return

def cmd_redo():
    tk.messagebox.showinfo(title='Info', message='Redo sth.')  # 提示信息对话窗
    return

menubar = tk.Menu(top_win)
menubar.add_command(label='Undo', command=cmd_undo)
menubar.add_command(label='Redo', command=cmd_redo)

frame = tk.Frame(top_win, width=400, height=300, bg='#ffccff')
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)
frame.bind("<Button-3>", popup)

#------------------------------


# show window and get into event loop
top_win.mainloop()
