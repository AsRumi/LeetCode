"""
3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Set-up the variables you will use:
        last_seen = {} # You need a dict to hold the last seen positions of all characters in the string
        left = 0 # This is the left index of the valid window that slides across the string
        # Between left and right, there are no repeating characters
        
        best = 0 # The highest window length ever recorded
        
        for right, ch in enumerate(s):
            
            # If this character has been seen before, and if its last-seen location falls INSIDE the window,
            # then this is a character you need to react to, since it makes the window invalid
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1 # Jump to the violating character's right, window becomes valid again
            last_seen[ch] = right # Update the last seen of the current character to current index
            best = max(best, right - left + 1)
        return best
    
answer = Solution()
longestSubstring = answer.lengthOfLongestSubstring(s = "pwwkew")
print(f"Longest Substring: {longestSubstring}")