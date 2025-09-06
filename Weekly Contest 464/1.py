class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even, oddSum, evenSum = 1, 2, 0, 0
        for i in range(n):
            oddSum += odd
            evenSum += even
            odd += 2
            even += 2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return gcd(oddSum, evenSum)
    
ans = Solution()
gcdOddEven = ans.gcdOfOddEvenSums(n = 4)
print(f"GCD Odd Even: {gcdOddEven}")