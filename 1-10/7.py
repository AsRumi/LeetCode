'''
You have to find the product of all the numbers of an array excluding the current number:
INPUT:  [1, 2, 3, 4]
OUTPUT: [24, 12, 8, 6]
You cannot use the division operator and time cimplexity must be O(n).

Could not solve: 6 mins 07 seconds
'''
'''
Solution: Initialize two lists with ones, one called prefix other called suffix.
In the prefix list, calculate the product of the immediate previous element and append it into the prefix array.
In the suffix list, calculate the product of the immediate successive element and append it into the suffix array.
Then for calculating the final product, take the previous value from the prefix array and the next value from the suffix array and multiply them.
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        suffix = []
        answer = []
        for i in range(0, len(nums)):
            prefix.append(1)
            suffix.append(1)
            answer.append(0)
        for p,i in enumerate(nums):
            if(p==0):
                prefix[p] = 1
                continue
            prefix[p] = nums[p-1]*prefix[p-1]
        last = len(nums) - 2
        suffix[len(nums) - 1] = 1
        while(last>=0):
            suffix[last] = nums[last+1] * suffix[last+1]
            last-=1
        for i in range(0, len(nums)):
            answer[i] = prefix[i] * suffix[i]
        return answer
    
answer = Solution()
my_list = answer.productExceptSelf([1, 2, 3, 4])
print(my_list)