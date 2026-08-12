"""
424. Longest Repeating Character Replacement https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Maintain a window which allows violations upto k
        
        # Set up the variables: 
        counts = defaultdict(int) # To count all occurances of given character in the window
        max_count = 0 # To store the value of most repeating character in the window
        left = 0 # left index of the window
        best = 0 # biggest window with violations allowed
        
        for right, ch in enumerate(s):
            
            counts[ch] += 1 # increment current char count
            max_count = max(max_count, counts[ch]) # store the count of char that repeats most
            # this is the char that we do not want to change (since it will cost the most)
            # all other characters will need to be changed and we have upto k changes to make
            
            # calculate how many characters are in the current window (from left to right inclusive)
            window_size = right - left + 1
                
            # if apart from the most repeating character, you have at most k violations (distinct characters) 
            # then your window is valid, otherwise you need to remove the character at the left-most position
            # and reduce its count (shrink the window)
            if window_size - max_count > k:
                counts[s[left]] -= 1
                left += 1

            # best length of the window seen so far
            best = max(best, right - left + 1)
            
        return best
    
answer = Solution()
characterReplacement = answer.characterReplacement(s = "ABAA", k = 0)
print(f"Character Replacement: {characterReplacement}")