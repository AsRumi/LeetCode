import math

class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        setNums = set(nums)
        result = 0
        
        # Find factors of each number:
        for x in nums:
            secondHalfFactors = []
            
            # Set the ending range by increasing one if it is an integer and taking the ceiling if it is not:
            sqrtRange = math.sqrt(x)
            sqrtRange = int(sqrtRange + 1) if sqrtRange % 1 == 0 else int(math.ceil(sqrtRange))
            
            flag = False
            
            for i in range(1, sqrtRange):
                if x % i == 0:
                    secondHalfFactors.append(x / i)
                    if i in setNums:
                        result += i
                        flag = True
                        break
                    
            # If the factor was found earlier, skip the iteration, else check with second half factors:
            if flag:
                continue
            else:
                while secondHalfFactors:
                    num = secondHalfFactors.pop()
                    if num in setNums:
                        result += num
                        break
        return int(result)
    
answer = Solution()
minArraySum = answer.minArraySum(nums = [4, 2, 8, 3])
print(f"Minimum Array Sum: {minArraySum}")