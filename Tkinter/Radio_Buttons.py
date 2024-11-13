from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("RadioButton tutorial")

def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()} from DesiBoyz. Thanks for ordering!")

var = StringVar()
var.set("Radio")

Label(root, text="What would you like to eat?", font="lucida 19 bold", justify=LEFT, padx=14).pack()

radio = Radiobutton(root, text="Chicken Karahi", padx=14, variable=var, value="Chicken Karahi").pack(anchor="w")
radio = Radiobutton(root, text="Chicken Biriyani", padx=14, variable=var, value="Chicken Biriyani").pack(anchor="w")
radio = Radiobutton(root, text="Butter Chicken", padx=14, variable=var, value="Butter Chicken").pack(anchor="w")
radio = Radiobutton(root, text="Chicken Tikka", padx=14, variable=var, value="Chicken Tikka").pack(anchor="w")

Button(text="Order Now", command=order).pack()

root.mainloop()