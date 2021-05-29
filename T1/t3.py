# Write a Python program to display the current date and time.

import datetime
from pprint import pprint

now = datetime.datetime.now()

print('current date and time : ')

print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%y-%m-%d %H:%M:%S"))
pprint(now.strftime("%D %T"))

