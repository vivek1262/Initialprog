import tkinter as tk
from tkinter.colorchooser import askcolor


def color():
    col = askcolor(color="#4621BF",title="My Colour Chooser")
    print(col)


root = tk.Tk()
root.iconbitmap(r'C:\Users\vishnu\Downloads\download.png')
tk.Button(root,text='Choose Color',fg="green",command=color).pack(side=tk.RIGHT, padx=10)
tk.Button(text='Quit',command=root.quit,fg="black").pack(side=tk.LEFT, padx=10)
tk.mainloop()