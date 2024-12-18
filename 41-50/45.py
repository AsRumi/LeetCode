# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if left == right:
                return True
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1
        return True
    
answer = Solution()
is_palindrome = answer.isPalindrome("A man, a plan, a canal: Panama")
print(f"Is Palindrome: {is_palindrome}")