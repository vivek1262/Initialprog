from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
root = Tk()
root.geometry("200x200")

def openfile():
    file = askopenfile(mode = 'r',filetypes = [('python files','*.py')])
    if file is not None:
        content = file.read()
        print(content)
Button(root,text = "Submit",command = lambda :openfile()).pack(side = TOP,pady = 10)


root.mainloop()