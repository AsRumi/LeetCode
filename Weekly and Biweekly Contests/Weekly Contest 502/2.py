import math
import time

class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        start = math.ceil(l**(1/k) - 1e-9)
        end = math.floor(r**(1/k) + 1e-9)
        return end - start + 1
    
answer = Solution()
startTime = time.perf_counter()
# kthRoots = answer.countKthRoots(l = 63015935, r = 436462053, k = 8)
kthRoots = answer.countKthRoots(l = 14, r = 16, k = 8)
endTime = time.perf_counter()

elapsedTime = endTime - startTime

print(f"Kth Roots in a Range: {kthRoots}")
print(f"Time taken: {elapsedTime}")