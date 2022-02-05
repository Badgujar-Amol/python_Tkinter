from tkinter import *

root = Tk()
root.geometry("400x200")
root.title('Refistration Form')

# heading
Label(root,text = "Registration Frorm",font = "ar 15 bold").grid(row=0,column=3)

#field nmae
first_name = Label(root, text = "First  Name")
last_name = Label(root, text = "Last  Name")
phone = Label(root, text = "Phone")
email = Label(root, text = "Email")
gender = Label(root, text = "Gender")

#packing fields
first_name.grid(row=1, column=2)
last_name.grid(row=2, column=2)
email.grid(row=3, column=2)
phone.grid(row=4, column=2)
gender.grid(row=5, column=2)

#variables for storing data
first_namevalue = StringVar
last_namevalue = StringVar
emailvalue = StringVar
phonevalue = StringVar
gendervalue = StringVar

#creating entry field
first_nameentry = Entry(root, textvariable = first_namevalue)
last_nameentry = Entry(root, textvariable = last_namevalue)
emailentry = Entry(root, textvariable = emailvalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)

#packing entey field
first_nameentry.grid(row=1, column=3)
last_nameentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
genderentry.grid(row=5, column=3)

#submit bbutton
btn = Button(root,text = 'Submit',fg='white', bg='#67be41').grid(row=6,column=3)

root.mainloop()
