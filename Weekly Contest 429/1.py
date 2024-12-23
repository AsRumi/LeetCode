# 3396. Minimum Number of Operations to Make Elements in Array Distinct

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen = set()
        n = len(nums)-1
        for i in range(n, -1, -1):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return (i//3)+1
        return 0
    
answer = Solution()
minimum_operations = answer.minimumOperations([1,2,3,4,2,3,3,5,7])
print(f"Minimum Operations: {minimum_operations}")