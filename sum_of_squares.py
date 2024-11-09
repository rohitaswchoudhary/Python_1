def sumofSquares(n):
    sm = 0
    for i in range(0,n+1):
        sm = sm + i*i
    
    return sm

n = 10000000
print(sumofSquares(n))