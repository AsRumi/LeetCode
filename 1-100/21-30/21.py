import math

class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        while n!=1:
            if n in hashSet:
                return False
            hashSet.add(n)
            n = sum([int(i)**2 for i in str(n)])
        else:
            return True
    
answer = Solution()
isHappy = answer.isHappy(2)
print(f"IS HAPPY? {isHappy}")