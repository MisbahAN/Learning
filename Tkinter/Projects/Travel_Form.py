from tkinter import *
import os

root = Tk()

root.geometry("644x344")

def getvals():
    print("Submitting Form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergency_contactvalue.get(), payment_modevalue.get(), food_servicevalue.get()}")

    # Determine the folder where the script is located
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "records.txt")

    with open(file_path, "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergency_contactvalue.get(), payment_modevalue.get(), food_servicevalue.get()}\n")

# Heading
Label(root, text="Welcome to Edmonton Travels", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

# Text for form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency_contact = Label(root, text="Emergency Contact")
payment_mode = Label(root, text="Payment Mode")

# Packing text using grid for form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency_contact.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

# Making variables to store string values
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergency_contactvalue = StringVar()
payment_modevalue = StringVar()

food_servicevalue = IntVar()

# Entries for our form 
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergency_contactentry = Entry(root, textvariable=emergency_contactvalue)
payment_modeentry = Entry(root, textvariable=payment_modevalue)

# Packing the entries using grid for form
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergency_contactentry.grid(row=4, column=3)
payment_modeentry.grid(row=5, column=3)

# Creating Checkbox and Packing it using grid for our form
foodservice = Checkbutton(text="Want to prebook your meals?", variable=food_servicevalue) # is 1 when box is ticked, else 0
foodservice.grid(row=6, column=3)

# Creating Button and Packing it using grid for our form
Button(text="Submit to Edmonton Travels", command=getvals).grid(row=7, column=3)

root.mainloop() 