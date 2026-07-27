class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        linearSum = 0
        squaredSum = 0
        for strDigit in str(n):
            digit = int(strDigit)
            linearSum += digit
            squaredSum += (digit * digit)
        if squaredSum - linearSum >= 50:
            return True
        return False
    
answer = Solution()
checkGoodInteger = answer.checkGoodInteger(n = 19)
print(f"Check Good Integer: {checkGoodInteger}")