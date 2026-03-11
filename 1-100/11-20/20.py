class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        counter = 0
        max_counter = 0
        money = k
        for p,i in enumerate(nums):
            next_p = p+1
            if(i==1):
                counter += 1
                while(next_p<len(nums)):
                    if(nums[next_p]==1):
                        counter+=1
                        next_p+=1
                    else:
                        if(money>0):
                            money-=1
                            counter+=1
                            next_p+=1
                        else:
                            money = k
                            break
                max_counter = counter if max_counter<counter else max_counter
                counter = 0
            else:
                if(money>0):
                    counter+=1
                    money-=1
                    while(next_p<len(nums)):
                        if(nums[next_p]==1):
                            counter+=1
                            next_p+=1
                        else:
                            if(money>0):
                                money-=1
                                counter+=1
                                next_p+=1
                            else:
                                money = k
                                break
                    max_counter = counter if max_counter<counter else max_counter
                    counter = 0
                else:
                    money = k
                    counter = 0
        return max_counter
    
answer = Solution()
greatestSeq = answer.longestOnes(nums = [0,0,1,1,1,0,0], k = 0)
print(f"Highest number of 1s: {greatestSeq}")