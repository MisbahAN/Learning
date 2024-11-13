from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Status Bar Tutorial")

def upload():
    statusvar.set("Busy..")
    root.update_idletasks()  # Update the GUI immediately
    root.after(2000, set_ready)  # Schedule 'set_ready' function to run after 2 seconds

def set_ready():
    statusvar.set("Ready")

statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w").pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

root.mainloop()