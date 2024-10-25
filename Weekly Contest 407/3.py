class Solution:
    def maxOperations(self, s: str) -> int:
        res = cnt = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "1" and s[i + 1] == "0": cnt += 1
            if s[i] == "1": res += cnt
        return res
    
answer = Solution()
maxOperations = answer.maxOperations(s = '101010101010')
print(f"Max Operations: {maxOperations}")