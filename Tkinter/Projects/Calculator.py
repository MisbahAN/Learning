from tkinter import *

# Create the main application window
root = Tk()
root.geometry("620x888")  # Set the window size
root.title("Calculator")  # Set the window title
root.wm_iconbitmap("Calculator.ico")  # Set the window icon to Calculator.ico

# Function to handle button click events
def click(event):
    global svalue
    text = event.widget.cget("text")  # Get the text of the clicked button

    # Handle "=" button to evaluate the expression
    if text == "=":
        try:
            value = eval(svalue.get())  # Evaluate the mathematical expression
        except Exception as e:
            value = "Error"  # If there's an error in the expression, display "Error"
        svalue.set(value)  # Set the result or error message on the screen
    
    # Handle "C" button to clear the screen
    elif text == "C":
        svalue.set("")  # Clear the screen
    
    # Handle other buttons to append text to the current expression
    else:
        svalue.set(svalue.get() + text)  # Add the clicked button's text to the current expression

# The screen (Entry widget) to display the current expression or result
svalue = StringVar()  # Create a StringVar to track the input expression
screen = Entry(root, textvariable=svalue, font="lucida 40 italic")  # Set the font and style for the screen
screen.pack(fill=X, padx=10, pady=5, ipadx=8)  # Pack the screen widget with padding

# Loop for buttons 1-9 in a grid pattern
x = 1
while x <= 7:
    f = Frame(root, bg="grey")  # Create a frame to hold the buttons
    
    # Button for numbers 1-3, 4-6, and 7-9 in each row
    for i in range(3):
        b = Button(f, text=str(x + i), padx=12, pady=12, font="lucida 35 bold", relief=RAISED)  # Create the button
        b.pack(padx=18, pady=18, side=LEFT)  # Pack the button within the frame
        b.bind("<Button-1>", click)  # Bind the click event to the button

    f.pack()  # Pack the frame containing the row of buttons
    x += 3  # Increment x to handle the next set of buttons

# Frame for the 0 button
f = Frame(root, bg="grey")
b = Button(f, text="0", padx=12, pady=12, font="lucida 35 bold", relief=RAISED)  # Create the 0 button
b.pack(padx=18, pady=18, side=LEFT)  # Pack the button within the frame
b.bind("<Button-1>", click)  # Bind the click event to the 0 button
f.pack()  # Pack the frame containing the 0 button

# Frame for miscellaneous buttons (e.g., C, /, %, *, =, +, -)
f = Frame(root, bg="grey")

# List of miscellaneous buttons
list1 = ["C", "/", "%", "*", "=", "+", "-"]
for item in list1:
    b = Button(f, text=str(item), padx=12, pady=12, font="lucida 35 bold", relief=RAISED)  # Create each miscellaneous button
    b.pack(padx=18, pady=18, side=LEFT)  # Pack the button within the frame
    b.bind("<Button-1>", click)  # Bind the click event to each button

f.pack()  # Pack the frame containing the miscellaneous buttons

# Run the main loop to display the GUI
root.mainloop()