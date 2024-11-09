class UserMainCode(object):
    @classmethod
    def numWays(cls, input1, input2):
        def factorial(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        n = input1
        k = input2
        numerator = factorial(n + k - 1)
        denominator = factorial(k - 1) * factorial(n)
        ans = numerator // denominator
        return ans
    
inp1 = int(input("input1: "))
inp2 = int(input("input2: "))
print(UserMainCode.numWays(inp1,inp2))