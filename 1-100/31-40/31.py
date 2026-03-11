#1957. Delete Characters to make Fancy String

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        if (len(s) == 3):
            if s[0] == s[1] == s[2]:
                return s[0] + s[1]
            else:
                return s
        fancy_string = ""
        fancy_string += s[0]
        position = 1
        while position < len(s)-1:
            if (s[position] == s[position-1]) and (s[position] == s[position+1]):
                position += 1
                continue
            fancy_string += s[position]
            position += 1
        return fancy_string + s[-1]
    
answer = Solution()
fancy_string = answer.makeFancyString(s = "leeetcode")
print(f"Fancy String: {fancy_string}")