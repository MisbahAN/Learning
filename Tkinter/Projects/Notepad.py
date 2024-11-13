import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to create a new file
def newFile():
    global file
    root.title("Untitled - Notepad")  # Set the title to "Untitled"
    file = None  # Reset the file to None (no file open)
    TextArea.delete(1.0, END)  # Clear the text area

# Function to open an existing file
def openFile():
    global file
    # Open file dialog to select a file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None  # If no file is selected, reset file variable
    else:
        root.title(os.path.basename(file) + " - Notepad")  # Set the window title to the file name
        TextArea.delete(1.0, END)  # Clear the text area
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())  # Insert the content of the file into the text area

# Function to save the current file
def saveFile():
    global file
    # If there's no file, open a save file dialog to create a new file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None  # If user cancels, reset file variable
        else:
            # Save the content to the file
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))  # Write the content of the text area to the file
            root.title(os.path.basename(file) + " - Notepad")  # Update the window title
            print("File saved")  # Print a message to console (optional)
    else:
        # If a file is already open, simply save it
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))  # Write the content of the text area to the file

# Function to quit the application
def quitApp():
    root.quit()  # Exit the Tkinter main loop and close the application

# Function to perform the cut operation (using the event_generate method)
def cut():
    TextArea.event_generate("<Control-x>")  # Simulate the cut command using Ctrl+X

# Function to perform the copy operation (using the event_generate method)
def copy():
    TextArea.event_generate("<Control-c>")  # Simulate the copy command using Ctrl+C

# Function to perform the paste operation (using the event_generate method)
def paste():
    TextArea.event_generate("<Control-v>")  # Simulate the paste command using Ctrl+V

# Function to display information about the application
def about():
    showinfo("Notepad", "Notepad by Misbah")  # Display a message box with app info

# Main part of the program
if __name__ == '__main__':
    # Initialize the Tkinter window
    root = Tk()
    root.title("Untitled - Notepad")  # Set the initial window title
    root.wm_iconbitmap("Notepad.ico")  # Set the application icon (optional)
    root.geometry("644x788")  # Set the size of the window

    # Create the text area where users can input text
    TextArea = Text(root, font="lucida 13")  # Define the text area widget with a specific font
    file = None  # Set the file variable to None initially
    TextArea.pack(expand=True, fill=BOTH)  # Add the text area to the window and make it expand

    # Create the menu bar at the top of the window
    MenuBar = Menu(root)

    # File menu with options like New, Open, Save, and Exit
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)  # New file command
    FileMenu.add_command(label="Open", command=openFile)  # Open file command
    FileMenu.add_command(label="Save", command=saveFile)  # Save file command
    FileMenu.add_separator()  # Separator for clarity
    FileMenu.add_command(label="Exit", command=quitApp)  # Exit the application
    MenuBar.add_cascade(label="File", menu=FileMenu)  # Add the File menu to the menu bar

    # Edit menu with Cut, Copy, and Paste options
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)  # Cut command
    EditMenu.add_command(label="Copy", command=copy)  # Copy command
    EditMenu.add_command(label="Paste", command=paste)  # Paste command
    MenuBar.add_cascade(label="Edit", menu=EditMenu)  # Add the Edit menu to the menu bar

    # Help menu with an About option
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)  # About command
    MenuBar.add_cascade(label="Help", menu=HelpMenu)  # Add the Help menu to the menu bar

    # Configure the root window to use the menu bar
    root.config(menu=MenuBar)

    # Add a scrollbar to the text area for easier navigation
    Scroll = Scrollbar(TextArea)  # Create a scrollbar widget
    Scroll.pack(side=RIGHT, fill=Y)  # Place the scrollbar on the right side of the text area
    Scroll.config(command=TextArea.yview)  # Link the scrollbar to the text area
    TextArea.config(yscrollcommand=Scroll.set)  # Configure the text area to use the scrollbar

    # Run the Tkinter main loop to display the window
    root.mainloop()