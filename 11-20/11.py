class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found = 0
        if(s==""):
            return True
        for i in t:
            if(i == s[found]):
                found += 1
            if(found == len(s)):
                break
        if(found == len(s)):
            return True
        return False

answer = Solution()
my_result = answer.isSubsequence(s = "", t = "ahbgdc")
print(my_result)
'''
found = 3
s = ace
      .
t = baicred
         .
'''