#3011. Find If Array Can Be Sorted

from collections import defaultdict
class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        """
        Main logic: If a swap is needed (using any algorithm) but cannot be facilitated because of a 
        mismatch of number of setbits, then return false, otherwise, return true.
        """
        def countSetBits(n):
            binary_n = str(bin(n))[2:]
            count = 0
            for n in binary_n:
                if n == "1":
                    count += 1
            return count
        
        n = len(nums)
        values = nums.copy()
        # Bubble Sort
        for i in range(n):
            for j in range(n-i-1):
                if values[j] <= values[j+1]:
                    continue
                else:
                    if countSetBits(values[j]) != countSetBits(values[j+1]):
                        return False
                    else:
                        values[j], values[j+1] = values[j+1], values[j]
        return True
    
answer = Solution()
can_sort_array = answer.canSortArray(nums = [8,4,2,30,15])
print(f"Can Sort Array: {can_sort_array}")