class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        counter = 0
        adder = 1
        position = -1
        while(counter<=k):
            position += adder
            if(position == n-1):
                adder = -1
            if(position == 0):
                adder = 1
            counter += 1
        return position

answer = Solution()
children = answer.numberOfChild(n = 4, k = 2)
print(f"Children: {children}")