class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals[1:]:
            cur_e = ans[-1][1]
            if s <= cur_e:
                ans[-1][1] = max(e, cur_e)
            else:
                ans.append([s, e])
        return ans