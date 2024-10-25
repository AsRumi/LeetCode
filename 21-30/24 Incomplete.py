# https://leetcode.com/problems/sentence-similarity-iii/?envType=daily-question&envId=2024-10-06

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        if len(sentence1)>len(sentence2):
            words1 = sentence1.split(" ")
            words2 = sentence2.split(" ")
        else: 
            words1 = sentence2.split(" ")
            words2 = sentence1.split(" ")
        if (len(words2)==1) and (words2[0]==words1[0] or words2[0]==words1[-1]):
            return True
        if len(words2) == 0:
            return True
        i = 0
        direction = "forward"
        while i<len(words1):
            if words1[i] == words2[i]:
                words2.remove(words2[i])
                if direction == "forward":
                    i+=1
                else:
                    i-=1
                if len(words2) == 0:
                    return True
            elif direction == "forward" and words1[i]!=words2[i]:
                direction = "backwards"
                i = -1
            else:
                pass
        return False
    
answer = Solution()
areSentencesSimilar = answer.areSentencesSimilar(sentence1="Eating right now doing something", sentence2="Eating right something")
print(f"Are sentences similar? {areSentencesSimilar}")