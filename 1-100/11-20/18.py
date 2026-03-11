
class Solution:
    def dayOfProgrammer(self, year: int) -> str:
        date = ""
        if(year<1918):
            date = "12.09."+str(year) if year%4==0 else "13.09."+str(year)
        elif(year == 1918):
            date = "30.08."+str(year)
        else:
            date = "12.09."+str(year) if ((year%4==0 and year%100!=0) or (year%400==0)) else "13.09."+str(year)
        return date

answer = Solution()
myDate = answer.dayOfProgrammer(1917)
print(f"256th day of the year is: {myDate}")