# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

print(abs.__doc__)

# Write a Python program to check whether a file exists.

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
print("                      ")



# Write a Python program to determine whether a Python shell is executing in 32bit or 64bit mode on OS?

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)
print("                  ")

# Write a Python program to get OS name, platform and release information.

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
print("                             ")


# Write a Python program to locate Python site-packages.

import site; 
print(site.getsitepackages())
print("                    ")

# Write a python program to call an external command in Python.

from subprocess import call
# call(["ls", "-l"])             # remove comment to execute.



# Write a python program to get the path and name of the file that is currently executing.

# import os
print("Current File Name : ",os.path.realpath(__file__))


# Write a Python program to find out the number of CPUs using.



import multiprocessing
print(multiprocessing.cpu_count())
