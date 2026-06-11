import math

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        
        def checkPrime(n):
            if n == 1:
                return 0
            limit = math.sqrt(n)
            limit = math.ceil(limit) if limit % 1 != 0 else limit + 1
            for i in range(2, int(limit)):
                if n % i == 0:
                    return 0
            return 1
        
        reversedNum = int(str(n)[::-1])
        l, r = min(n, reversedNum), max(n, reversedNum)
        sum = 0
        for i in range(l, r + 1):
            if checkPrime(i):
               sum += i 
        return sum
    
answer = Solution()
sumOfPrimes = answer.sumOfPrimesInRange(n = 10)
print(f"Sum of Primes: {sumOfPrimes}")