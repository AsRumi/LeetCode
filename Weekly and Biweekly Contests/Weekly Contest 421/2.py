# 3335. Total Characters in String After Transformations

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cycles = t//26
        leftover_t = t-(cycles*26)
        initial_freq = {}
        for i in range(97, 123):
            initial_freq[chr(i)] = 0
        for letter in s:
            initial_freq[letter] += 1
        next_freq = initial_freq.copy()
        for i in range(cycles):
            for j in range(97, 123):
                if j == 97:
                    next_freq[chr(j)] = ((initial_freq[chr(j)] * 2) + initial_freq['z']) % (10**9+7)
                    continue
                elif j == 98:
                    next_freq[chr(j)] = ((initial_freq[chr(j)] * 2) + initial_freq['a'] + initial_freq['z']) % (10**9+7)
                    continue
                next_freq[chr(j)] = ((initial_freq[chr(j)] * 2) + initial_freq[chr(j-1)]) % (10**9+7)
            initial_freq = next_freq.copy()
        i = 122
        while i >= 97+26-leftover_t:
            next_freq['a'] += next_freq[chr(i)]
            next_freq['b'] += next_freq[chr(i)]
            next_freq[chr(i)] = 0
            i -= 1
        total_characters = 0
        for i in next_freq.values():
            total_characters += i
        return total_characters % (10**9 + 7)
    
answer = Solution()
length_after_transformations = answer.lengthAfterTransformations(s = "jqktcurgdvlibczdsvnsg", t = 7517)
print(f"Length after transformations: {length_after_transformations}")