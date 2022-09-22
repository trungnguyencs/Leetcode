class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        removedS, removedE = toBeRemoved
        for s, e in intervals:
            if s < removedS:
                ans.append([s, min(e, removedS)])
            if e > removedE:
                ans.append([max(s, removedE), e])
        return ans