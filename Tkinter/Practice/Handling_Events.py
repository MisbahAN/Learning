from tkinter import *

def message(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text="Click me")
widget.pack()

# Search Tkinter events on google
widget.bind('<Button-1>', message)
widget.bind('<Double-1>', quit)

root.mainloop()