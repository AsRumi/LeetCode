class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        ans = False
        position = 0
        while(position<len(flowerbed)):
            if(position == len(flowerbed)-1):
                if(flowerbed[position-1] == 0 and flowerbed[position] != 1):
                    count += 1
                    break
            if(flowerbed[position] == 1):
                position += 2
            else:
                if(flowerbed[position+1] == 1):
                    position += 3
                else:
                    position += 2
                    count += 1
        if(count >= n):
            ans=True
        return ans
    
answer = Solution()
my_flower_bed = answer.canPlaceFlowers([0,0,1,0,0], 1)
print(my_flower_bed)