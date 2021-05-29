# Write a Python program to display the first and last colors from the following list

color_list = ["Red", "Green", "White", "Black"]

print((color_list[0], color_list[-1]))

# Write a Python program to print out a set containing all the colors from color_list_1
# which are not present in color_list_2.

color_list_1 = {"White", "Black", "Red", "Yellow", "Orange"}
color_list_2 = {"Red", "Green"}

print(color_list_1.difference(color_list_2))
