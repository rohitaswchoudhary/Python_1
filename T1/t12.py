# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(22))
print(difference(14))

print("                   ")


# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_thousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

print("                       ")


# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.


def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

print("                            ")


# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))

print("                       ")


# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum


print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

print("                      ")


# Write a Python program which will return true if the two given integer
# values are equal or their sum or difference is 5.

def test_number5(x, y):
    if x == y or abs(x - y) == 5 or (x + y) == 5:
        return True
    else:
        return False


print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))

print("                          ")


# Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b


print(add_numbers(10, 20))
print("                  ")

# Write a Python program to solve (x + y) * (x + y).

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))
