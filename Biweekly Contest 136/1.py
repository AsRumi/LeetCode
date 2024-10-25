from collections import Counter
class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        players = dict()
        winningCount = 0
        for [player, ball] in pick:
            if player in players.keys():
                players[player].append(ball)
            else:
                players[player] = [ball]
        for player, balls in players.items():
            counter = Counter(balls)
            highestBallsCollected = counter.most_common(1)[0]
            if highestBallsCollected[1] > player:
                winningCount += 1
        return winningCount
                
answer = Solution()
winningPlayers = answer.winningPlayerCount(n = 2, pick = [[1,3],[1,3],[0,10],[1,6]])
print(f"Winning Players Count: {winningPlayers}")