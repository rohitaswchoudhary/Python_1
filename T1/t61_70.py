# 2021-06-10 17:44:04

# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.4f miles." % d_miles)


# Write a program to convert all units of time into seconds.


days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)

# write a program to get absolute file path.

import time
import os.path
from pathlib import Path
p = Path("\\T1\\t50_60.py").resolve()
print(p)

# Write a Python program to get file creation and modification date/times.


print("Last modified: %s" % time.ctime(os.path.getmtime("abc.txt")))
print("Created: %s" % time.ctime(os.path.getctime("abc.txt")))


# Write a Python program to calculate body mass index.

height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

# write a program to convert pressure in various units.


kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))


# OR 

kpa= float(input("Input the pressure in kilopascals > "))
pressure_in_psi = round(kpa * 0.145038,3)
pressure_in_mmHg = round(kpa * 7.50062, 3)
pressure_in_atmp = round(kpa * 0.0098692382432766,3)
print(f"Pressure = {pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")


# Calculate the sum of the digits in an integer

num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


# Function to get sum of digits  

def getSum1(n): 
     
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
    
n1 = 12345
print(getSum1(n1))



#  Using sum() methods.: The sum() method is used to sum of numbers in the list.

def getSum2(n): 
      
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
    
n2 = 12345
print(getSum2(n2))


def getSum3(n): 
     
    sum = 0
    while (n != 0): 
        
        sum = sum + (n % 10)
        n = n//10
        
    return sum
    
n3 = 12345
print(getSum3(n3))



def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))


# Driver code
n4 = 12345
print(sumDigits(n4))



# Write a Python program to sort three integers without using conditional statements and loops.

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print(f"Numbers in sorted order: {a1} < {a2} < {a3}")

import os
os.chdir('d:')
result = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
print('\n'.join(map(str, result)))


import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))
