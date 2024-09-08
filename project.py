mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123password",
    database="testdb",
)
mycursor = mydb.cursor()

sqlFormula = "INSERT INTO students(name, age) VALUES (%s, %s)"
from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")
# Heading
Label(root, text="School Admission Portal",font="ar 15 bold").grid(row=0, column=3)

# Field Name
Name = Label(root, text="Name")
Phone = Label(root, text="Phone")
Gender = Label(root, text="Gender")
Emergency = Label(root, text="Emergency")
PaymentMode = Label(root, text="Payment Mode")

# Packing Fields
Name.grid(row=1, column=2)
Phone.grid(row=2, column=2)
Gender.grid(row=3, column=2)
Emergency.grid(row=4, column=2)
PaymentMode.grid(row=5, column=2)

# Variable For Storing Data
nameValue =StringVar
phoneValue =StringVar
genderValue =StringVar
EmergencyValue =StringVar
PaymentModeValue =StringVar
checkvalue =IntVar

# Creating Entry fields
nameentry =Entry(root, textvariable =nameValue)
phoneentry =Entry(root, textvariable =phoneValue)
genderentry =Entry(root, textvariable =genderValue)
Emergencyentry =Entry(root, textvariable =EmergencyValue)
paymentModeentry =Entry(root, textvariable =PaymentModeValue)

# Packing Entry Fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
Emergencyentry.grid(row=4,column=3)
paymentModeentry.grid(row=5,column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

# Submit Button
Button(text="submit", command=getvals).grid(row=7, column=3)
root.mainloop()