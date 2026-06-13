from collections import defaultdict

class Solution:
    def sortVowels(self, s: str) -> str:
        # Count vowels in a dictionary and create an indices list:
        s = list(s)
        countDict = defaultdict(int)
        indices = []
        
        for i, char in enumerate(s):
            if char in ['a', 'e', 'i', 'o', 'u']:
                indices.append(i)
                countDict[char] += 1
        
        # Sort the defaultdict based on values:
        sorted_dict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse = True))
        
        # Insert the vowels into the indices:
        i = 0
        for key, value in sorted_dict.items():
            while value > 0:
                value -= 1
                s[indices[i]] = key
                i += 1
            
        return "".join(s)
    
answer = Solution()
sortVowels = answer.sortVowels(s = "leetcode")
print(f"Sort Vowels: {sortVowels}")