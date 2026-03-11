# 22. Generate Parentheses

'''
class Solution:
    def __init__(self):
        self.stack = []
        
    def generateParenthesis(self, n: int) -> list[str]:
        def generateNewSingle(string = '(', opening = n-1, closing = n):
            if opening == 0 and closing == 0:
                self.stack.append(string)
                return
            if opening == 0:
                string += ')'
                closing -= 1
                generateNewSingle(string, opening, closing)
            else:
                added_opening = string + '('
                new_opening = opening - 1
                generateNewSingle(string = added_opening, opening = new_opening, closing = closing)
                added_closing = string + ')'
                new_closing = closing - 1
                generateNewSingle(string = added_closing, opening = opening, closing = new_closing)
            return string
        if n == 1:
            self.stack.append('()')
            return self.stack
        generateNewSingle(string = '(', opening = n-1, closing = n)
        return self.stack
'''

class Solution:
    def __init__(self):
        self.stack = []
        
    def generateParenthesis(self, n: int) -> list[str]:
        def generateNewSingle(string, opening, closing):
            if opening == closing and opening + closing == n*2:
                self.stack.append(string)
                return
            if opening < n:
                generateNewSingle(string = string + '(', opening = opening + 1, closing = closing)
            if closing < opening:
                generateNewSingle(string = string + ')', opening = opening, closing = closing + 1)
        generateNewSingle("", 0, 0)
        return self.stack
    
answer = Solution()
generated = answer.generateParenthesis(n = 4)
print(f"Generated Paranthesis: {generated}")