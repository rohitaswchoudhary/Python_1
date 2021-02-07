# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

print("                    ")


# Write a Python program to display your details like name, age, address in three different lines.

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()
