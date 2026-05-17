from typing import List
class Solution:
    def minDifference(self, n: int, k: int):
        num = n**(1/k)
        if num.is_integer():
            res = []
            for i in range(k):
                res.append(int(num))
            return res
        res = []
        for i in range(k-1):
            res.append(1)
        res.append(n)
        current = max(res) - min(res)
        minimum = max(res)
        while current < minimum:
            minimum = current
            for i in range(2, max(res)):
                if max(res)%i == 0:
                    res[0] = res[0]*i
                    res[-1] = int(res[-1]/i)
                    res.sort()
                    break
            current = max(res) - min(res)
        return res
    
    def minDifferenceClaude(self, n: int, k: int) -> List[int]:
        factors = []
        temp = n
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        while len(factors) < k:
            factors.append(1)
        result = [1] * k
        factors.sort(reverse=True)
        for factor in factors:
            min_idx = result.index(min(result))
            result[min_idx] *= factor
        return sorted(result)
    
ans = Solution()
minDiff = ans.minDifferenceClaude(n = 45, k = 2)
print(f"Minimum Difference = {minDiff}")