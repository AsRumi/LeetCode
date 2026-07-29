"""
509. Fibonacci Number: https://leetcode.com/problems/fibonacci-number/description/
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        first, second = 1, 0
        result = 0
        for i in range(2, n + 1):
            result = first + second
            second = first
            first = result
        return result
    
answer = Solution()
fib = answer.fib(n = 4)
print(f"Fib: {fib}")