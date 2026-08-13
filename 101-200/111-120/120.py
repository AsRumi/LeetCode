"""
567. Permutation in String https://leetcode.com/problems/permutation-in-string/description/
"""

from collections import Counter
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window approach: maintain a need, matches, and a counter
        
        # Set up variables:
        need = Counter(s1)
        required = len(need)
        length = len(s1)
        counter = defaultdict(int)
        matches = 0
        left = 0

        for right, ch in enumerate(s2):
            # Increment count of every char
            counter[ch] += 1
            
            # If current char rose to match the target
            if ch in need and counter[ch] == need[ch]:
                matches += 1

            # When window overgrows, shrink it one from the right
            # In the shrink step, you only need to check if removing the current char 
            # resulted in that char reducing matches by one or no
            if right - left + 1 > length:
                left_ch = s2[left]
                if left_ch in need and counter[left_ch] == need[left_ch]:
                    matches -= 1 # about to fall below target
                counter[left_ch] -= 1
                left += 1

            # Check if current window is valid or not
            if matches == required:
                return True
        
            # Expand step is handled by the for loop itself

        return False
    
answer = Solution()
checkInclusion = answer.checkInclusion(s1 = "adc", s2 = "dcda")
print(f"Check Inclusion: {checkInclusion}")