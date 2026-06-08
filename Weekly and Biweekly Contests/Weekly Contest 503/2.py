class Solution:
    def passwordStrength(self, password: str) -> int:
        
        strength = 0
        # Create a set:
        setChars = set()
        
        for char in password:
            
            if (ord(char) >= ord('a') and ord(char) <= ord('z')) and char not in setChars:
                strength += 1
                setChars.add(char)
            if (ord(char) >= ord('A') and ord(char) <= ord('Z')) and char not in setChars:
                strength += 2
                setChars.add(char)
            if (ord(char) >= ord('0') and ord(char) <= ord('9')) and char not in setChars:
                strength += 3
                setChars.add(char)
            if (char in ['!', '@', '#', '$']) and char not in setChars:
                strength += 5
                setChars.add(char)
        
        return strength
    
answer = Solution()
passwordStrength = answer.passwordStrength(password = "aA1!")
print(f"Password Strength: {passwordStrength}")