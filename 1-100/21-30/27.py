# 1657. Determine if two strings are close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = {}
        dict2 = {}
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        for letter in word1:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1
        for letter in word2:
            if letter not in dict2:
                dict2[letter] = 1
            else:
                dict2[letter] += 1
        dict2 = dict(sorted(dict2.items(), key = lambda item: item[1]))
        dict1 = dict(sorted(dict1.items(), key=lambda item: item[1]))
        for (_, value1), (_, value2) in zip(dict1.items(), dict2.items()):
            if value1 != value2:
                return False
        return True
    
answer = Solution()
closeStrings = answer.closeStrings(word1 = "uau", word2 = "ssx")
print(f"Close Strings: {closeStrings}")