# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.


values = input("Input some comma separated numbers : ")
list1 = values.split(",")
tuple1 = tuple(list1)
print('List : ', list1)
print('Tuple : ', tuple1)
