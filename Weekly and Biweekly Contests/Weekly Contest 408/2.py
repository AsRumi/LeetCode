class Solution:
    def __init__(self):
        self.notSpecialSet = set()
    def nonSpecialCount(self, l: int, r: int) -> int:
        def checkNotSpecial(num):
            if num == 1 or num == 2:
                return True
            divisors = 1
            for i in range(2, num):
                if num % i == 0:
                    divisors += 1
                if divisors > 2:
                    return True
            if divisors != 2:
                return True
            return False
        def addMultiples(num, r):
            start = 1
            while(num<r):
                num *= start
                start += 1
                self.notSpecialSet.add(num)
        notSpecial = 0
        r += 1
        for i in range(l, r):
            if i == 4:
                continue
            if i in self.notSpecialSet:
                notSpecial += 1
                continue
            if checkNotSpecial(i):
                notSpecial += 1
                addMultiples(num = i, r = r)
            else:
                continue
        return notSpecial
    
answer = Solution()
nonSpecialCount = answer.nonSpecialCount(l = 2, r = 4)
print(f"Non Special Count: {nonSpecialCount}")