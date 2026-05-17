class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = ""
        continous = True
        for p,c in enumerate(s):
            if p < len(s)-1:
                c_d = int(c)
                n_d = int(s[p+1])
                if c_d%2==n_d%2 and c_d > n_d:
                    ans += str(n_d)
                    ans += str(c_d)
                    ans += s[p+2:]
                    continous = False
                    break
                else:
                    ans += str(c_d)
        if continous:
            ans += s[-1]
        return ans
    
answer = Solution()
smallestString = answer.getSmallestString(s = "001")
print(f"Smallest String: {smallestString}")