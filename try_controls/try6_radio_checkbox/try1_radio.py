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

var_sel=tk.IntVar()
var_sel.set(0)
text_of_btn=('北京','广州','上海','深圳')
value_of_btn=(0,1,2,3)
'''
def show_selected():
    print('---')
    print(v1.get())
    return

chk_btn1=tk.Checkbutton(
        frame_root1,
        text=text_of_btn[0],
        variable=value_of_btn[0],
        command=show_selected
        )
chk_btn1.place(x=20,y=40)
'''
def show_selected():
    v=var_sel.get()
    print(text_of_btn[v])
    return
for idx in range(4):
    rad_btn=tk.Radiobutton(
            frame_root1,
            variable=var_sel,
            text=text_of_btn[idx],
            value=value_of_btn[idx],
            command=show_selected
            )
    rad_btn.place(x=20 + idx * 190 , y=40)
#------------------------------


# show window and get into event loop
top_win.mainloop()
