class Solution:
    def reverseWords(self, s: str) -> str:
        list_words = s.split()
        list_words.reverse()
        final_string = " ".join(list_words)
        return final_string
    
answer = Solution()
reversed_words = answer.reverseWords(s="HELLO WORLD")
print(reversed_words)