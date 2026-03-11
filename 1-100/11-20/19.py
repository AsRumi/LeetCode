class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        insertPointer = len(nums1)-1
        secondPointer = len(nums2)-1
        firstPointer = m - 1
        while(secondPointer>=0 and firstPointer>=0):
            if(nums1[firstPointer] <= nums2[secondPointer]):
                nums1[insertPointer] = nums2[secondPointer]
                insertPointer -= 1
                secondPointer -= 1
            else:
                nums1[insertPointer] = nums1[firstPointer]
                insertPointer -= 1
                firstPointer -= 1
        while(secondPointer>=0):
            nums1[insertPointer] = nums2[secondPointer]
            secondPointer -= 1
            insertPointer -= 1
        
answer = Solution()
answer.merge(nums1=[2, 0], m = 1, nums2=[1], n=1)