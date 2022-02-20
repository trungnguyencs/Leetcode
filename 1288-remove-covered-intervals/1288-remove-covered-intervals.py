class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: [x[0], -x[1]]) #ascending start, descending end
        removedCount, prevEnd = 0, float('-inf')
        for s, e in intervals:
            if e <= prevEnd:
                removedCount += 1
            else:
                prevEnd = e
        return len(intervals) - removedCount