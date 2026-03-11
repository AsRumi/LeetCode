# 769. Max Chunks To Make Sorted

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return 1
        prefixMax = [arr[0]]
        suffixMin = [0] * (len(arr) - 1)
        suffixMin.append(arr[-1])
        for i in range(1, len(arr)):
            prefixMax.append(max(arr[i], prefixMax[i-1]))
        for i in range(len(arr)-2, -1, -1):
            suffixMin[i] = (min(suffixMin[i+1], arr[i]))    
        chunks = 0
        for i in range(len(arr)):
            if i == 0 or prefixMax[i-1] < suffixMin[i]:
                chunks += 1
        return chunks
    
answer = Solution()
max_chunks = answer.maxChunksToSorted(arr = [0,1])
print(f"Max Chunks: {max_chunks}")