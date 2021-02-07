# Write a Python program which accepts the radius of a circle from the user and compute the area.


from math import pi
r = float(input ("Input the radius of the circle : "))
print (f"The area of the circle with radius {r}  is: {pi * r**2} ")

# Write a Python program to get the the volume of a sphere with radius 6.

pi = 3.1415926535897931
V= 4.0/3.0*pi* r**3
print(f'The volume of the sphere with radius {r} is ',V)

# Write a Python program that will accept the base and height of a triangle and compute the area.

b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)
