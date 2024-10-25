class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        changes = 0
        binaryn = bin(n)[2:]
        binaryk = bin(k)[2:]
        while len(binaryk) < len(binaryn):
            binaryk = '0' + binaryk
        while len(binaryn) < len(binaryk):
            binaryn = '0' + binaryn
        for pos, bit in enumerate(binaryn):
            if bit == '0' and binaryk[pos] == '1':
                changes = -1
                break
            if bit == '1' and binaryk[pos] == '0':
                changes += 1
        return changes
        
        
answer = Solution()
minChanges = answer.minChanges(n = 13, k = 4)
print(f"Minimum Changes: {minChanges}")