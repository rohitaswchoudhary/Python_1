# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("enter the integer: "))
print("\nthe value of n+n*n+n*n*n is : ",n+n**2+n**3)


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# Write a Python program to find whether a given number (accept from the user) is even or odd, 
# print out an appropriate message to the user.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# Write a Python program to count the number 4 in a given list.

def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))


# Write a Python program to check whether a specified value is contained in a group of values.

def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))