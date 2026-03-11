class Solution:
    def clearStars(self, s: str) -> str:
        list_ans = list(s)
        smallest = 0
        for p,l in enumerate(list_ans):
            smallest = p
            if(l=="*"):
                while(p>=0):
                    if s[p] < s[smallest]:
                        smallest = p
                    else:
                        break
                    p-=1
                list_ans.remove(list_ans[p])
                list_ans.remove(list_ans[smallest])
        return list_ans.join("")

answer = Solution()
myString = answer.clearStars(s="aaba*")
print(myString)