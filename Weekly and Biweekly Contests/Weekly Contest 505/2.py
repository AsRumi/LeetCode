class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        validStrings = []
        
        def stringGenerator(currentString, currentCost):
            nonlocal validStrings
            
            # Base case: Length Reached
            if len(currentString) == n:
                validStrings.append(currentString)
                return
            
            # Recursive calls:
            else:
                
                # If starting with an empty string:
                if len(currentString) == 0:
                    stringGenerator(currentString + '0', currentCost)
                    stringGenerator(currentString + '1', currentCost)
                    
                # Conditions meet so call both:
                elif currentString[-1] == '0' and len(currentString) <= currentCost:
                    stringGenerator(currentString + '0', currentCost)
                    stringGenerator(currentString + '1', currentCost - len(currentString))
                
                # Conditions not met, call only 0:
                else:
                    stringGenerator(currentString + '0', currentCost)
        
        stringGenerator('', k)
        
        return validStrings
    
answer = Solution()
listValidStrings = answer.generateValidStrings(n = 3, k = 1)
print(f"List of Valid Strings: {listValidStrings}")