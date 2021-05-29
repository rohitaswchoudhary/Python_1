# Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str


print(new_string("Array"))
print(new_string("IsEmpty"))


# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def larger_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))


# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))


# Write a Python program to test whether a passed letter is a vowel or not.


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))
