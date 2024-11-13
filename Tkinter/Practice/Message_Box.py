"""Code imported from Menu.py and also appended for Message Box"""

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("VSCode")

def myfunc():
    print("Hello im Undar da Wader please help me")

def help():
    print("I will help you!")
    a = tmsg.showinfo("Help", "Misbah will help you with this GUI!")
    print(a) # Returns ok by default

def rateus():
    print("Rate us :)")
    value = tmsg.askquestion("Your Experience with us.", "Was your GUI experience satisfactory with us?")

    if value == "yes":
        msg = "Great! Rate us on AppStore please!"
    else:
        msg = "Tell us what went wrong."

    tmsg.showinfo("Experience", msg)

    print("Was the users experience with us good?", value) # Returns yes/no by default

    # can use many tmsg methods, common one is askretrycancel

mainmenu = Menu(root)

# Creating m1
m1 = Menu(mainmenu, tearoff = 0) # wont let you remove submenu from the GUI
# Adding commands for m1
m1.add_command(label="New Poject", command=myfunc)
m1.add_separator()
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Save As", command=myfunc)
m1.add_separator()
m1.add_command(label="Print", command=myfunc)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
# packing the menu
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

# Creating m2
m2 = Menu(mainmenu, tearoff = 0) # wont let you remove submenu from the GUI
# Adding commands for m2
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Find", command=myfunc)
m2.add_separator()
m2.add_command(label="Exit", command=quit)
# packing the menu
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

# Creating m3
m3 = Menu(mainmenu, tearoff = 0) # wont let you remove submenu from the GUI
# Adding commands for m3
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rateus)
# packing the menu
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

root.mainloop() 