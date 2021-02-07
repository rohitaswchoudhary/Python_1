# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

# Write a Python program to print the calendar of a given month and year.

# Python calendar.month(theyear, themonth, w=0, l=0):

# The function returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

# 'l' specifies the number of lines that each week will use.

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# Write a Python program to print the following 'here document'.

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
