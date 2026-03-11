class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        sum = [1] * n
        for t in range(k):
            for i in range(1, n):
                sum[i] = (sum[i] + sum[i-1]) % 1000000007
        return sum[-1]

answer = Solution()
value = answer.valueAfterKSeconds(n = 4, k = 5)
print(f"Value: {value}")