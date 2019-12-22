import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class UC_Show:
    def __init__(self,pwin):

        print('UC_Show class create!')
        self.parent_win = pwin

        # naming root window
        self.parent_win.title('Show - By Class')
        # resize root window
        win_size_pos = '800x600'
        #win_size_pos = '360x60'
        self.parent_win.geometry(win_size_pos)

        self.__init_widgets()

        return

    def __init_widgets(self):
        self.lbl_info=tk.Label(
            self.parent_win,
            text='Show form',
            anchor="w",
            justify="left",
            bg='#ffccff',
            fg='#ff0099',
            height=1
        )
        self.lbl_info.place(x=20,y=20,width=200)


        return
