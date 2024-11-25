# 3341. Find Minimum Time to reach Last Room

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        def moveRight(moveTime, currentPosition, time=0):
            if currentPosition == [len(moveTime) - 1, len(moveTime[0]) - 1]:
                return 1 + max(0, moveTime[currentPosition[0]][currentPosition[1]] - time)
            if currentPosition[0] == len(moveTime) - 1:
                nextPosition = [currentPosition[0], currentPosition[1] + 1]
                move_right_time = max(time + 1, moveTime[nextPosition[0]][nextPosition[1]])
                return 1 + moveRight(moveTime, nextPosition, move_right_time)
            if currentPosition[1] == len(moveTime[0]) - 1:
                nextPosition = [currentPosition[0] + 1, currentPosition[1]]
                move_down_time = max(time + 1, moveTime[nextPosition[0]][nextPosition[1]])
                return 1 + moveDown(moveTime, nextPosition, move_down_time)
            rightPosition = [currentPosition[0], currentPosition[1] + 1]
            downPosition = [currentPosition[0] + 1, currentPosition[1]]
            move_right_time = max(time + 1, moveTime[rightPosition[0]][rightPosition[1]])
            move_down_time = max(time + 1, moveTime[downPosition[0]][downPosition[1]])
            return min(1 + moveRight(moveTime, rightPosition, move_right_time),
                       1 + moveDown(moveTime, downPosition, move_down_time))
        
        def moveDown(moveTime, currentPosition, time=0):
            if currentPosition == [len(moveTime) - 1, len(moveTime[0]) - 1]:
                return 1 + max(0, moveTime[currentPosition[0]][currentPosition[1]] - time)
            if currentPosition[1] == len(moveTime[0]) - 1:
                nextPosition = [currentPosition[0] + 1, currentPosition[1]]
                move_down_time = max(time + 1, moveTime[nextPosition[0]][nextPosition[1]])
                return 1 + moveDown(moveTime, nextPosition, move_down_time)
            if currentPosition[0] == len(moveTime) - 1:
                nextPosition = [currentPosition[0], currentPosition[1] + 1]
                move_right_time = max(time + 1, moveTime[nextPosition[0]][nextPosition[1]])
                return 1 + moveRight(moveTime, nextPosition, move_right_time)
            rightPosition = [currentPosition[0], currentPosition[1] + 1]
            downPosition = [currentPosition[0] + 1, currentPosition[1]]
            move_right_time = max(time + 1, moveTime[rightPosition[0]][rightPosition[1]])
            move_down_time = max(time + 1, moveTime[downPosition[0]][downPosition[1]])
            return min(1 + moveRight(moveTime, rightPosition, move_right_time),
                       1 + moveDown(moveTime, downPosition, move_down_time))
        
        return moveRight(moveTime, [0, 0], time=0)
    
answer = Solution()
min_time = answer.minTimeToReach(moveTime = [[0,4],[4,4]])
print(f"Minimum Time to Reach Last Room: {min_time}")