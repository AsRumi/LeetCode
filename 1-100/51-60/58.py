# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for n in nums1:
            position = nums2.index(n) + 1
            greater_number = -1
            while position < len(nums2):
                if nums2[position] > n:
                    greater_number = nums2[position]
                    break
                position += 1
            result.append(greater_number)
        return result
    
answer = Solution()
next_greater = answer.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
print(f"Next Greater Element: {next_greater}")