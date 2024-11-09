def binomial_coefficients(n, m):
    res = 1
    if m > n - m:
        m = n - m
    for i in range(m):
        res *= (n - i)
        res /= (i + 1)
    return res

def calc_ways(m, n):

    if m == 1:
        return n
    if m < n:
        return 0
    ways = binomial_coefficients(n + m - 1, n - 1)
    return int(ways)

m = int(input("input1: "))
n = int(input("input2: "))
print(calc_ways(m, n))