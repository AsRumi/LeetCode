'''
Compress a character array in the following manner: aaaabbbbb -> a4b5

Solved: 8 Minutes
'''

class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        my_string = ""
        for i in range(1, len(chars)):
            if(chars[i-1] == chars[i]):
                count = count + 1
            else:
                my_string = my_string + chars[i-1] + str(count)
                count = 1
        my_string = my_string + chars[-1] + str(count)
        chars = list(my_string)
        return chars

answer = Solution()
my_length = answer.compress(["a", "a", "a", "b", "b", "b", "b", "b"])
print(my_length)