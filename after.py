from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
from time import time

root = Tk()

button = Button(root, text = 'Button').pack(side = TOP, pady = 5)

print('Running...')
start = time()
root.after(4000, root.destroy)
mainloop()
end = time()
print('Destroyed after % d seconds' % (end-start))