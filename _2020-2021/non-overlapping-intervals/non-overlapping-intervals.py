class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removedCount = 0
        lastEnd = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= lastEnd:
                lastEnd = e
            else:
                removedCount += 1
                lastEnd = min(lastEnd, e)
        return removedCount