# 20. Valid Parenthesis

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        key = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for bracket in s:
            if bracket in ('(', '{', '['):
                brackets.append(bracket)
            else:
                if len(brackets) == 0:
                    return False
                if brackets[-1] == key[bracket]:
                    brackets.pop()
                else:
                    return False
        if len(brackets) != 0:
            return False
        return True
    
answer = Solution()
is_valid = answer.isValid(s=  "()[]{}")
print(f"Is Valid: {is_valid}")