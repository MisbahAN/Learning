from tkinter import*

root = Tk()

root.geometry("655x333")

frame1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
frame1.pack(side=LEFT, fill="y")

frame2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
frame2.pack(side=TOP, fill="x")

label1 = Label(frame1, text = "Project Tkinter - PyCharm")
label1.pack(pady=142)

label2 = Label(frame2, text = "Welcome to sublime text", font="Helvetica 16 bold", fg="red")
label2.pack()

root.mainloop() 