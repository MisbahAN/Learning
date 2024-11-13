from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("VSCode GUI")

root.wm_iconbitmap("VSCode_logo.ico")
root.configure(background="cyan")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command= root.destroy).pack()

root.mainloop()