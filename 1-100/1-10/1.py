class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString =""
        list1 = list(word1)
        list2 = list(word2)
        while(len(list1) > 0 and len(list2) >0):
            mergedString=mergedString+list1[0]+list2[0] # apbqcr
            list1.remove(list1[0])
            list2.remove(list2[0])
        if(len(list1)>0):
            for i in list1:
                mergedString += i
        if(len(list2)>0):
            for i in list2:
                mergedString += i
        return mergedString
answer = Solution()
my_String = answer.mergeAlternately(word1="abcdef", word2="pqr")
print(my_String)