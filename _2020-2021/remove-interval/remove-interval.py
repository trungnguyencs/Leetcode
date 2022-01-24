class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        i = 0
        ans = []
        removedS, removedE = toBeRemoved
        while i < len(intervals) and intervals[i][1] <= removedS:
            ans.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] < removedE:
            if intervals[i][0] < removedS:
                ans.append([intervals[i][0], removedS])
            if intervals[i][1] > removedE:
                ans.append([removedE, intervals[i][1]])
            i += 1
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        return ans
    
    # def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    #     ans = []
    #     removedS, removedE = toBeRemoved
    #     for s, e in intervals:
    #         if s < removedS:
    #             ans.append([s, min(e, removedS)])
    #         if removedE < e:
    #             ans.append([max(s, removedE), e])
    #     return ans