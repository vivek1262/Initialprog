from tkinter import *
from tkinter import messagebox
def exitMe():
    if getboolean(messagebox.askyesno("confirm to exit", "ok", icon='info')):
        exit()

def check():
    name=messagebox.askquestion("Questioner" , "Is this your name",icon = 'info')
    if (name=="yes"):
        exitMe()
    else:
        print("Name is not same")


window = Tk()

window.geometry("100x100")
Button(window , text = "Vivek" , command = check).pack()

window.mainloop()