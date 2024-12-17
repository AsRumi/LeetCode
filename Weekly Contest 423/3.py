class Solution:
    def sumOfGoodSubsequences(self, nums: list[int]) -> int:
        arr_len, mod_ = max(nums) + 2, 1_000_000_007
        cnt, good = [0] * arr_len, [0] * arr_len
        for num in nums:
            change = (1 + cnt[num - 1] + cnt[num + 1]) %mod_
            cnt[num]+= change
            good[num]+= good[num - 1] + good[num + 1] + num * change
            good[num]%= mod_
        return sum(good) %mod_
    
answer = Solution()
sum = answer.sumOfGoodSubsequences(nums = [1, 2, 6, 7, 8, 3, 2, 1])
print(f"Sum of good subsequences: {sum}")