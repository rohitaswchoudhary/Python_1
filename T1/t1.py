print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a Diamond in the sky.')

# Write a Python program to print the following 'here document'.
'''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

print(
'''
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
'''
    
)


# Write a Python program to parse a string to Float or Integer.

n="256.258756"
print(n,type(n))

print(float(n),type(float(n)))
print(int(float(n)),type(int(float(n))))
# print(type(int(float(n))))