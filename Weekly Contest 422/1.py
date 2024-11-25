# 3340. Check Balanced String

class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_sum = 0
        even_sum = 0
        i = 0
        while(i<len(num)):
            if i%2==0:
                even_sum += int(num[i])
            else:
                odd_sum += int(num[i])
            i += 1
        return True if odd_sum == even_sum else False
    
answer = Solution()
is_balanced = answer.isBalanced(num = "1234")
print(f"Is Balanced: {is_balanced}")