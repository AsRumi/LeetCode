"""
1025. Divisor Game: https://leetcode.com/problems/divisor-game/description/
"""

class Solution:
    def divisorGame(self, n: int) -> bool:
        # Dynamic Programming Approach
        winStatus = {1: False,
                     2: True,
                     3: False}
        if n <= 3: return winStatus[n]
        for i in range(4, n + 1):
            divisors = [d for d in range(1, i // 2 + 1) if i % d == 0]
            for divisor in divisors:
                given = i - divisor
                if given in winStatus.keys() and winStatus[given] == False:
                    winStatus[i] = True
                    print(f"Win Status updated to set {i} to True.\nYou win {i} by giving opponent {given}.\nCurrent Win Status = {winStatus}")
                    break
            if not(i in winStatus.keys()):
                winStatus[i] = False 
                print(f"Win Status updated to set {i} to False.\nCurrent Win Status = {winStatus}")
        return winStatus[n]
    
answer = Solution()
divisorGame = answer.divisorGame(n = 6)
print(f"Divisor Game: {divisorGame}")