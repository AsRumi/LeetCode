'''
days = 10
[[5, 7], [1, 3], [9, 10]]
[[1, 3], [5, 7], [9, 10]]
[[1, 2], [1, 4], [7, 10]]
[[]]
'''

class Solution:
    def countDays3(self, days, meetings):
        meetings = [meeting for meeting in meetings if meeting[1]<=days]
        meetings.sort(key=lambda x:x[0]) # Only sorting the list based on the first element of the meetings array.
        # If you have [[3, 7], [1, 4], [1, 2]] --> Sorted as --> [[1, 4], [1, 2], [3, 7]]
        # Does not even check the second element to compare.
        n = len(meetings)
        r = days
        i = 0
        while(i < n):
            p = [meetings[i][0], meetings[i][1]]
            print(f"Present day range: {p}")
            while i+1<n and meetings[i+1][0] <= p[1]: # First condition to not breach the length of the array;
                # Second condition to check if the second set of meeting has start day coming before the current end day to modify the range.
                # This handles the overlap of the meetings.
                p[1] = max(p[1], meetings[i+1][1])
                print(f"Adjusted day range: {p}")
                i += 1
            r -= p[1] - p[0] + 1 # Total number of days worked (inclusive) = End Day - First Day + 1
            i += 1
        return r

answer = Solution()
days = answer.countDays3(days = 10, meetings = [[1, 4],[2, 5],[6, 9]])
print(days)