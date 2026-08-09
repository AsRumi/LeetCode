"""
Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/description/
"""

from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Sliding window setup:
        
        need = Counter(t) # builds a Counter of how many times each character must appear
        window = defaultdict(int) # defaultdict because we use count of characters that we have never seen before
        matches = 0 # to keep a track of how many characters in the window currently satisfy the target condition
        
        # total number of characters whose counts must match target
        required = len(need) # len(Counter) returns number of keys
        
        left = 0 # left counter to keep a track of what is being removed during the shrink step
        
        best_l = 0 # best left and right locations
        minimum_length = float('inf') # smallest length which gives best left and best right
        
        for right, ch in enumerate(s): # expand window to the right
            window[ch] += 1 # increment the count of current character that just entered the window
            
            # Now you need to check if the character that just entered results in satisfying any condition of target:
            if ch in need and window[ch] == need[ch]:
                matches += 1
            """
            You only have the above condition because only that is relevant.
            Example: If 2 As are needed, then count matches target when we have two A's in the window, so you increment matches.
            And as soon as As become 3, they don't match target anymore, but the window is still valid because you can get 
            2 As out of 3 As. The shrinking logic will handle what happens to excess As on the left side of the window.
            """
            
            """
            Now as soon as you have the required number of matches, start shrinking from the left.
            Shrink until you remove a character that violates matches == required,
            which would mean that character was needed to complete the target.
            Store that target and continue moving the right side of the window.
            """
            while matches == required:
                
                # Store this answer only if it beats the current best minimum window
                if right - left + 1 < minimum_length:
                    minimum_length = right - left + 1
                    best_l = left
                
                left_ch = s[left]
                
                if left_ch in need and window[left_ch] == need[left_ch]:
                    matches -= 1 # removing this character broke the condition
                    
                window[left_ch] -= 1
                left += 1
                    
        if minimum_length == float('inf'):
            return ""
        
        return s[best_l: best_l + minimum_length] # return best length and the minimum length that was recorded from that left index
    
answer = Solution()
minWindow = answer.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(f"Min Window: {minWindow}")