class Solution:
    def minimumChairs(self, s: str) -> int:
        e_positions = []
        count = 0
        max = 0
        for p,i in enumerate(s):
            if(i=="E"):
                e_positions.append(p)
        for i in range(e_positions[0],e_positions[-1]+1):
            print(s[i], end="")
            if(s[i]=='E'):
                count += 1
                max = count if max<count else max
            else:
                count -= 1
        return max

answer = Solution()
chairs = answer.minimumChairs(s="EEEEEELELLLE")
print(chairs)