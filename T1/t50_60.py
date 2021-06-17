from __future__ import print_function
import socket
import getpass
import os
import sys
import cProfile
import timeit
import time


# 1.) program to get the execution time of a function or a script.


# 2.)  write a program to print without newline or space.
def fun1():
    for i in range(0, 10):
        print("*", end="")


print("\n")

cProfile.run("fun1()")

execution_time1 = timeit.timeit(fun1, number=1)

print("\n", execution_time1)


# 3.) Write a Python program to determine profiling of Python programs.

'''
A profile is a set of statistics that describes how often and for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.
'''


def sum():
    print(1+2)


cProfile.run("sum()")

execution_time = timeit.timeit(sum, number=1)

print(execution_time)


# 4.) write a program to print to stderr.


def eprint(*args, **kwargs):

    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep="--")


# 5.) write a program to access environment variables.


# access all environment variables

print('*-----------------------------------*')
print(os.environ)
print('*--------------------------------*')
# print(os.environ['HOME'])
print('*-----------------------------------*')
print(os.environ['PATH'])
print('*-----------------------------------*')


# 6.)  write a program to get the current user Name.


print(getpass.getuser())


# 7.)  Write a Python program to find local IP address using Python's stdlib.


print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                                                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                                                                                                                 socket.SOCK_DGRAM)]][0][1]]) if l][0][0],"\n\n")


# Python Program to Get IP Address


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is :" + hostname)
print("Your Computer IP Address is: " + IPAddr)



# 8.)  Write a Python program to get terminal size(width and height).

# this program is for non windows user as windows dont have fcntl support.

# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

# print('Number of columns and Rows: ',terminal_size())


# for windows users(use get_terminal_size() method):

start_time = time.time()

size = os.get_terminal_size()


print("\n\n",size)

end_time = time.time()

print(end_time-start_time)

# 58.)  write a program to print Sum of first n positive integers.

n = int(input("enter the number upto which \n you want to get the sum : "))

sum = (n*(n+1))/2

print(f"sum of first {n} positive integers is :", sum)

# 59.)  write a program to convert height to centimeters.

print("\n\nEnter your height:")
h_feet = int(input("Feet: "))
h_inches = int(input("Inches: "))

h_inches += h_feet*12

h_centi = round(h_inches*2.54, 2)

print("\nYour height in centimeters is : ", h_centi)

# program to find absolute file path.

def absolute_file_path(path_fname):
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("abc.txt"))

from math import sqrt

print("Enter base and height of a right triangle.")

a = float(input("enter length of base: "))
b = float(input("enter length of height: "))

c = sqrt(a**2 + b**2)
print("Length of hypotenuse is : ",c)
