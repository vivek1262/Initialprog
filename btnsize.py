from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox
top = Tk()


def Button_1():
    messagebox.showinfo("Status","Button-1 Pressed")


def Button_2():
    messagebox.showinfo("Status","Button-2 Pressed")


top.geometry("100x100")
B1 = Button(top, text="Button-1",command=Button_1)
B2 = Button(top, text="Button-2",command=Button_2)

B1.pack()
B2.pack()
top.mainloop()
