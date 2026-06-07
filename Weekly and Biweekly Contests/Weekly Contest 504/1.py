from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        counter_n = Counter(str(n))
        sum = 0
        for key, value in counter_n.items():
            sum += int(key) * value
        return sum
    
answer = Solution()
digitFreqScore = answer.digitFrequencyScore(n = 122)
print(f"Digit Frequency Score = {digitFreqScore}")