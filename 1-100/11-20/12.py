'''
Solved but time inefficient, have to make the code run faster.
'''
'''
Idea to make the code faster:
Find the max height of the pole from the array and store its position. 
If there are multiple poles with the same height, store all their positions.
Then you only need one loop to check all the poles with the max height poles.

Problem: Not all the times is the highest pole going to give you the biggest area: Example 1, 2, 1 since the 1s span greater in length.
'''
'''
Code from LeetCode:
Initialize two pointers, left and right.
Find area at these pointers and check with max area.
Check left and right pointers, if left is smaller, bring left to right.
If right is smaller, bring right to left.
If left becomes greater than right, stop the loop.
This way you make sure you only compare the highest poles for area.
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        max_area = 0
        while(i<=len(height)-2):
            j = i+1
            while(j<=len(height)-1):
                area = min(height[i], height[j]) * (j-i)
                if(area>max_area):
                    max_area = area
                j+=1
            i+=1
        return max_area
    
    def maxAreaGreedy(self, height: list[int]) -> int:
        max_height = max(height)
        biggest_poles = []
        max_area = 0
        for p,i in enumerate(height):
            if(i==max_height):
                biggest_poles.append((p,i))
        for biggest_position,biggest_pole in biggest_poles:
            for position,pole in enumerate(height):
                area = min(biggest_pole, pole) * abs(biggest_position - position)
                if(max_area<area):
                    max_area = area
        return max_area
    
answer = Solution()
my_maxArea = answer.maxAreaGreedy(height=[1, 2, 1])
print(f"Maximum area of water = {my_maxArea} units")