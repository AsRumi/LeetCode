"""
67. Add Binary https://leetcode.com/problems/add-binary/description/?envType=problem-list-v2&envId=bit-manipulation
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        answer = ""
        carry = False
        counter = 0
        for i in range(min(len(a), len(b))):
            if a[i] == '0' and b[i] == '0':
                if carry:
                    answer += '1'
                    carry = False
                else:
                    answer += '0'
            elif a[i] == '0' or b[i]== '0':
                if carry:
                    answer += '0'
                else:
                    answer += '1'
            else:
                if carry:
                    answer += '1'
                else:
                    answer += '0'
                    carry = True
            counter += 1
            
        while counter < len(a):
            if carry:
                if a[counter] == '0':
                    answer += '1'
                    carry = False
                else:
                    answer += '0'
            else:
                answer += a[counter]
            counter += 1
            
        while counter < len(b):
            if carry:
                if b[counter] == '0':
                    answer += '1'
                    carry = False
                else:
                    answer += '0'
            else:
                answer += b[counter]
            counter += 1
        
        if carry:
            answer += '1'
        return answer[::-1]
    
    
answer = Solution()
addBinary = answer.addBinary(a = "1", b = "111")
print(f"Add binary: {addBinary}")