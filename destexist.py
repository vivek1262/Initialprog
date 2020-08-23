from tkinter import *
from tkinter.ttk import *

root = Tk()
def destroy(widget):
    widget.destroy()
    print("Destroy method called.widget exist?=",bool(widget.winfo_exists()))
def exist(widget):
    print("Checking for existance = ",bool(widget.winfo_exists()))

root.title("Window")
root.geometry("200x200")
b1 = Button(root, text="Button 1")
b1.pack(fill = BOTH,expand=True)

print(" in Middle of the program")
b2 = Button(root, text="Button 2",command = lambda :destroy(b1)).pack(fill = BOTH,expand =True)

b3 = Button(root,text = "Button 3",command = lambda :exist(b1)).pack(fill = BOTH,expand =True)
mainloop()
