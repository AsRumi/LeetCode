# 2490. Circular Sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if words[0][0] != words[-1][-1]:
            return False
        for (position, word) in enumerate(words):
            if position == len(words)-1:
                break
            if word[-1] != words[position+1][0]:
                return False
        return True
    
answer = Solution()
is_circular_sentence = answer.isCircularSentence(sentence = "IuTiUtGGsNydmacGduehPPGksKQyT TmOraUbCcQdnZUCpGCYtGp p pG GCcRvZDRawqGKOiBSLwjIDOjdhnHiisfddYoeHqxOqkUvOEyI")
print(f"Is Circular Sentence: {is_circular_sentence}")