class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        curStart, curEnd = meetings[0]
        for i in range(1, len(meetings)):
            s, e = meetings[i]
            if s > curEnd:
                days -= curEnd - curStart + 1
                curStart, curEnd = s, e
            else:
                curEnd = max(curEnd, e)
        days -= curEnd - curStart + 1
        return days