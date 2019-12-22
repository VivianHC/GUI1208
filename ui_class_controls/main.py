import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


from gui_class_login import UC_Login

from gui_class_show import UC_Show
# create root window
root = tk.Tk()
from_login=UC_Login(root)
root.mainloop()
root.destroy()

# create root window
root = tk.Tk()
from_show=UC_Show(root)
root.mainloop()
