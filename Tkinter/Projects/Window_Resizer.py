from tkinter import *

def resize(l, b):
    global initialized
    initialized = True

    root.geometry(f"{b}x{l}")

def dele(event):
    if le.get()=="LENGTH":
        length_entry.delete(0,END)
        length_entry.configure(fg="black")

def dele2(event):
    if  wi.get()=="WIDTH":
        width_entry.delete(0,END)
        width_entry.configure(fg="black")

def col(event):
    if not initialized:
        return
    width = event.width
    height = event.height
    red = min(255, int(width / 5))
    green = min(255, int(height / 5))
    blue = min(255, int((width + height) / 10))
    color = f'#{red:02x}{green:02x}{blue:02x}'
    root.config(bg=color)
    root.update_idletasks()

root = Tk()
root.title("Window Resizer")
root.configure(bg='yellow')
initialized = False
le = StringVar()
length_entry = Entry(root, textvariable=le,fg="grey")
length_entry.insert(0, "LENGTH")
# length_entry.pack(side='center',padx=10,pady=10,anchor='center')

wi = StringVar()
width_entry = Entry(root, textvariable=wi,fg="grey")
width_entry.insert(0, "WIDTH")
# width_entry.pack(padx=10,pady=10,anchor='center')

b=Button(root,text="ENTER",command=lambda: resize(le.get(),wi.get()))
width_entry.place(relx=0.5, rely=0.3, anchor='center')
length_entry.place(relx=0.5, rely=0.4, anchor='center')
b.place(relx=0.5, rely=0.5, anchor='center')

entry_width = max(length_entry.winfo_width(), width_entry.winfo_width())
button_width = b.winfo_width()


# Calculate the minimum size
min_width = max(entry_width, button_width) 

# Set the minimum size of the window
root.minsize(min_width, 1)


length_entry.bind('<FocusIn>',dele)
width_entry.bind('<FocusIn>',dele2)
root.bind('<Configure>',col)


root.mainloop()