# 735. Asteroid Collision

from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stackOfAsteroids = deque()
        stackOfAsteroids.append(asteroids[0])
        del asteroids[0]
        similar = False
        for item in asteroids:
            if (len(stackOfAsteroids) == 0):
                stackOfAsteroids.append(item)
                continue
            if (item/stackOfAsteroids[-1] < 0) and (item<0):
                while (len(stackOfAsteroids) > 0) and (abs(item) >= abs(stackOfAsteroids[-1])):
                    if item == stackOfAsteroids[-1]:
                        stackOfAsteroids.append(item)
                        break
                    elif abs(item) == abs(stackOfAsteroids[-1]):
                        stackOfAsteroids.pop()
                        similar = True
                        break
                    if stackOfAsteroids[-1] < 0:
                        stackOfAsteroids.append(item)
                        break
                    stackOfAsteroids.pop()
                if len(stackOfAsteroids) > 0 and stackOfAsteroids[-1] < 0 and item < 0 and not similar and not(stackOfAsteroids[-1] == item):
                    stackOfAsteroids.append(item)
                if (len(stackOfAsteroids) > 0):
                    similar = False
                    pass
                else:
                    if similar:
                        similar = False
                        pass
                    else:
                        stackOfAsteroids.append(item)
            else:
                stackOfAsteroids.append(item)
        i = 0
        total = len(stackOfAsteroids)
        ans = []
        while i<total:
            i+=1
            ans.append(stackOfAsteroids.popleft())
        return ans
    
answer = Solution()
asteroidCollision = answer.asteroidCollision(asteroids = [-2, -2, 1, -2])
print(f"Asteroid Collision: {asteroidCollision}")