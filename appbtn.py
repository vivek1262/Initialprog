from tkinter import *


root = Tk()
root.title("window")
root.geometry("250x250")
L = Label(root,text = "DELL")
L.pack()
checkbutton1 = IntVar()
checkbutton2 = IntVar()
checkbutton3 = IntVar()

b1 = checkbutton(root,text = "name",variable = checkbutton1, onvalue = 1,offvalue = 0,height = 2,width = 10)
b1.pack()
b2 = checkbutton(root,text = "age",variable = checkbutton2,onvalue = 1,offvalue = 0,height = 2,width = 10)
b2.pack()
b3 = checkbutton(root,text = "color",variable = checkbutton3,onvalue = 1,offvalue = 0,height = 2,width = 10)
b3.pack()


root.mainloop()