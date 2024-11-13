from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Graph of Y against X")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point (x1, y1) to (x2, y2) denoted as (x1, y1, x2, y2) 
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="blue")

# Specify coordinates in this order - coord top left, coord bott right
can_widget.create_rectangle(200, 100, 600, 50, fill="yellow")

# Uses same coordinates as rectangle to create oval inside rectangle
can_widget.create_oval(200, 100, 600, 50, fill="green")

can_widget.create_text(400, 75, text="Python")

root.mainloop()