from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider tutorial")

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited", f"We have credited {myslider2.get()} dollars to your bank account")

"""myslider1 = Scale(root, from_=0, to=100) # Vertical be default
myslider1.pack()"""

Label(root, text="How many $'s do you want?")
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50) # tickinterval allows only multiples of 50
myslider2.set(10) # Sets initial value for Slider scale
myslider2.pack()

Button(root, text="Get $'s!", pady=10, command=getdollar).pack()

root.mainloop()