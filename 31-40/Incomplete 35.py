#3011. Find If Array Can Be Sorted

class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        unsorted_binary_list = [str(bin(n))[2:] for n in nums]
        print(unsorted_binary_list)
        nums.sort()
        sorted_binary_list = [str(bin(n))[2:] for n in nums]
        print(sorted_binary_list)
        return False
    
answer = Solution()
can_sort_array = answer.canSortArray(nums = [6, 7, 13, 2, 8, 6])
print(f"Can Sort Array: {can_sort_array}")