from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Listbox Tutorial")

i = 0

def additem():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item")

Button(root, text="Add item", command=additem).pack()

root.mainloop()