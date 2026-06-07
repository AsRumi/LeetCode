class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sumGood = 0
        rangeLow, rangeHigh = n - k, n + k
        rangeLow = 1 if rangeLow <= 0 else rangeLow
        for i in range(rangeLow, rangeHigh + 1):
            if (n & i == 0):
                sumGood += i
        return sumGood