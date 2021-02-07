# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

amt = 10000
int = 3.5
years = 7

future_value  = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))
print("                      ")


# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

print("                         ")


