# 150. Evaluate Reverse Polish Notation
import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operands = ['*', '/', '+', '-']
        for t in tokens:
            if t in operands:
                if t == '*':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 * num2)
                elif t == '/':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    result = num1 / num2
                    if result < 0:
                        stack.append(math.ceil(result))
                    else:
                        stack.append(math.floor(result))
                elif t == '+':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 + num2)
                else:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 - num2)
            else:
                stack.append(int(t))
        return stack[0]
    
answer = Solution()
eval_rpn = answer.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(f"Eval RPN: {eval_rpn}")