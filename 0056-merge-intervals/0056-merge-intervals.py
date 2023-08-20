class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals[1:]:
            lastE = ans[-1][1]
            if s > lastE:
                ans.append([s, e])
            else:
                ans[-1][1] = max(e, lastE)
        return ans