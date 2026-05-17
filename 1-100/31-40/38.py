from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for word in strs:
            anagram = "".join(sorted(word))
            result[anagram].append(word)
        return list(result.values())
    
answer = Solution()
groups = answer.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
print(f"Group Anagrams: {groups}")