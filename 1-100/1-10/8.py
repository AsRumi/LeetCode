'''
Increasing Triplet Subsequence: You are supposed to find if a triplet in an array such that:
i < j < k and arr[i] < arr[j] < arr[k] exists.
If it does, then return true, otherwise return false.
Edge Case: i, j, and k do not have to be consecutive. [10, 12, 5, 13] should pass the test too!

Solved: 14 mins 10 seconds but time complexity is really bad.
'''

'''
Time optimized solution: O(n)
Take two arrays and initialize them with such values:
min_array stores the lowest element recorded up till that index position.
Example: [1, 5, 0, 4, 1, 3]'s min_array would be [1, 1, 0, 0, 0, 0]
max_array goes backwards and stores the highest element recorded up till that index position.
Example: [1, 5, 0, 4, 1, 3]'s max_array would be [3, 3, 4, 4, 5, 5]
Now we reverse the max_array.
Therefore our 3 arrays are:
[1, 1, 0, 0, 0, 0]
[1, 5, 0, 4, 1, 3]
[5, 5, 4, 4, 3, 3]
Now we simply compare at each iteration is min_array(i) < array(i) < max_array(i):
'return True' if it is.
else 'return False'
'''

class Solution:
    def increasingTripletBadTimeComplexity(self, nums:list[int]) -> bool:
        pointer = 0
        if(len(nums)<3):
            return False
        while(pointer<=len(nums)-3):
            i = pointer+1
            while(i<=len(nums)-2):
                if(nums[pointer]<nums[i]):
                    j = i+1
                    while(j<len(nums)):
                        if(nums[i]<nums[j]):
                            return True
                        j += 1
                i += 1
            pointer += 1
        return False
    
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False

        min_arr = []
        for num in nums:
            if min_arr and num > min_arr[-1]:
                min_arr.append(min_arr[-1])
            else:
                min_arr.append(num)

        max_arr = []
        for num in nums[::-1]:
            if max_arr and num < max_arr[-1]:
                max_arr.append(max_arr[-1])
            else:
                max_arr.append(num)
        max_arr = max_arr[::-1]

        for i in range(1, len(nums) - 1):
            if min_arr[i] < nums[i] < max_arr[i]:
                return True

        return False
    
answer = Solution()
my_bool = answer.increasingTripletBadTimeComplexity([20, 100, 10,12,5,13])
print(my_bool)