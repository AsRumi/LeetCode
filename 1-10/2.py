import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        if(str1 == str2):
            gcd = str1
        elif(str1+str2 == str2+str1):     
            gcd = str1[:math.gcd(len(str1), len(str2))] # Using the mathematical GCD formula on the length of both the strings.
        else:
            pass
        return gcd
    
answer = Solution()
my_GCD = answer.gcdOfStrings(str1="ABCABC", str2="ABCABC")
print(my_GCD)