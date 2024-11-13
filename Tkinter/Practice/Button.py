from tkinter import *

root = Tk()
root.geometry("655x333")

frame = Frame(root, borderwidth=6, bg="grey", relief =SUNKEN)
frame.pack(side=LEFT, anchor="nw")

def hello():
    print("hello from tkinter GUI")

bl = Button(frame, fg="red", text="Print now", command=hello)
bl.pack(side=LEFT)

b2 = Button(frame, fg="red", text="Print now")
b2.pack(side=LEFT, padx=100)

b3 = Button(frame, fg="red", text="Print now")
b3.pack(side=LEFT, padx=100)

b4 = Button(frame, fg="red", text="Print now")
b4.pack(side=LEFT, padx=100)

root.mainloop()