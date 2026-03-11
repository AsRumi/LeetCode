class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        positions = []
        reversed = list(s)
        for p,i in enumerate(s):
            if(i in vowels):
                positions.append(p)
        og_p = positions.copy()
        positions.reverse()
        for p,i in enumerate(og_p):
            reversed[i] = s[positions[p]]
        reversed_vowels = "".join(reversed)
        return reversed_vowels
    
answer =  Solution()
vowels_reversed = answer.reverseVowels(s="LEETCODE")
print(vowels_reversed)