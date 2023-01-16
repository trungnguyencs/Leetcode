class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newS, newE = newInterval
        ans = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newS:
            ans.append(intervals[i])
            i += 1
        ans.append(newInterval)
        while i < len(intervals) and intervals[i][0] <= newE:
            ans[-1] = [min(ans[-1][0], intervals[i][0]), max(ans[-1][1], intervals[i][1])]
            i += 1
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        return ans