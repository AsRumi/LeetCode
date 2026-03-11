# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temp_stack = []
        result = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            if len(temp_stack) == 0:
                temp_stack.append(day)
                continue
            else:
                while len(temp_stack) > 0 and temperatures[temp_stack[-1]] < temp:
                    result[temp_stack[-1]] = day - temp_stack[-1]
                    temp_stack.pop()
            temp_stack.append(day)
        return result
    
answer = Solution()
daily_temperatures = answer.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
print(f"Daily Temperatures: {daily_temperatures}")