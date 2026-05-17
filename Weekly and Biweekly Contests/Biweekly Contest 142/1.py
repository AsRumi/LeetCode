class Solution:
    def possibleStringCount(self, word: str) -> int:
        if len(set(word)) == len(word):
            return 1
        repeat_count = 0
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                repeat_count += 1
        return repeat_count + 1
    
answer = Solution()
possibleStringCount = answer.possibleStringCount(word = "ere")
print(f"Possible string count: {possibleStringCount}")