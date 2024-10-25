class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a","e","i","o","u"]
        list_1 = []
        for letter in s:
            if letter in vowels:
                list_1.append(1)
            else:
                list_1.append(0)
        max = sum(list_1[0:k])
        prev = max
        i = 1
        while i<= len(s)-k:
            current_sum = prev - list_1[i-1] + list_1[i+k-1]
            prev = current_sum
            max = current_sum if current_sum>max else max
            if(max == k):
                return max
            i+=1
        return max

answer = Solution()
myMaxVowels = answer.maxVowels(s="abciiidef", k=3)
print(f"Max vowels in a substring: {myMaxVowels}")