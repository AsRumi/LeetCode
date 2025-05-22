"""
875. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def calculateHours(piles, speed):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/speed)
            return hours
        
        maxSpeed = max(piles)
        minSpeed = 1
        
        while(minSpeed < maxSpeed):
            targetSpeed = (minSpeed + maxSpeed) // 2
            hoursTaken = calculateHours(piles, targetSpeed)
            if hoursTaken <= h:
                maxSpeed = targetSpeed
            else:
                minSpeed = targetSpeed + 1
        return minSpeed
    
# def calculateHours(piles, speed):
#     hours = 0
#     for bananas in piles:
#         hours += math.ceil(bananas/speed)
#     return hours
    
# print(calculateHours(piles = [3, 6, 7, 11], speed = 6))
# print(round(11/2))
answer = Solution()
minEatingSpeed = answer.minEatingSpeed(piles = [3,6,7,11], h = 8)
print(f"Min Eating Speed: {minEatingSpeed}")