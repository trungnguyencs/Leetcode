class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xIntervals = []
        yIntervals = []
        for startX, startY, endX, endY in rectangles:
            xIntervals.append([startX, endX])
            yIntervals.append([startY, endY])
        mergedXIntervals = self.mergeIntervals(xIntervals)
        mergedYIntervals = self.mergeIntervals(yIntervals)
        return len(mergedXIntervals) >= 3 or len(mergedYIntervals) >= 3

    def mergeIntervals(self, intervals):
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals:
            if s >= ans[-1][1]:
                ans.append([s, e])
            else:
                ans[-1][1] = max(ans[-1][1], e)
        return ans