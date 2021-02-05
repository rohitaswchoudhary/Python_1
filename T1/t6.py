# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.


values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
