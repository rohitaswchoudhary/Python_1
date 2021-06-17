# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
print("Hello  " + last_name + " " + first_name)

print("                    ")


# Write a Python program to display your details like name, age, address in three different lines.

def personal_details(name, age):

    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


name = input('enter your name:')
age = input('enter you age:')

personal_details(name, age)

f=open("abc.txt", "w")

a="rohit choudhary"

f.write(a)
f.close()
