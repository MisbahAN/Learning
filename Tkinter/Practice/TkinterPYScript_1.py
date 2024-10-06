from tkinter import *

my_first_gui = Tk() # Creates a basic GUI with the basic functions

# Dimensions of GUI
my_first_gui.geometry("800x400") # "LengthxWidth" of the deafult GUI (parameters are in "")
my_first_gui.minsize(800, 400) # Restricting the min size of the GUI
my_first_gui.maxsize(1000, 500) # Restricting the max size of the GUI

# Appearance 
my_first_gui.title("My first GUI") # Adds a title for the GUI

FirstLine_Label = Label(my_first_gui, text = "This is my first ever line written on a GUI!", bg = "cyan", fg = "black", padx = 50, pady = 50, font = ("comicsansms", 19, "bold"), borderwidth = 3, relief = SUNKEN) # self-explanatory, search internet for different fonts and releif values
FirstLine_Label.pack(side = BOTTOM, fill = Y) # side, anchor, fill (X and Y)

TempImage = PhotoImage(file = "VSCode_logo.png") # Adding image file to GUI
TempImage_Label = Label(my_first_gui, image = TempImage) # Creating a label for the image
TempImage_Label.pack() # This makes the object "TempImage_Label" visible on the GUI

my_first_gui.mainloop()
