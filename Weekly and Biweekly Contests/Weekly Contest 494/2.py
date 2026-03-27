"""
3876. Construct Uniform Parity Array II https://leetcode.com/problems/construct-uniform-parity-array-ii/description/
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        smallest_even = (nums1[0] % 2 == 0)
        seen_odd, seen_even = None, None
        if smallest_even:
            seen_even = True
        else:
            seen_odd = True
        i = 1
        while i < len(nums1):
            if seen_odd and seen_even and not smallest_even:
                return True
            if smallest_even and not (nums1[i] % 2 == 0) and not seen_odd:
                return False
            if nums1[i] % 2 == 0:
                seen_odd = True
            else:
                seen_even = True
            i += 1
        return True