# find the GCD of the two number.


def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print("gcd: ", gcd(12, 10000))
print("gcd: ", gcd(4, 6))

print("""                          
                               """
      )


# LCM of two numbers.

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while (True):
        if (z % x == 0) and (z % y == 0):
            lcm = z
            break
        z += 1

    return lcm


print("lcm: ", lcm(4, 6))
print("lcm: ", lcm(15, 17))
