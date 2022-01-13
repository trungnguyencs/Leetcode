class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        curEnd = float(-inf)
        arrows = 0
        points.sort(key=lambda x: x[1]) #shoot the ending soonest
        for s, e in points:
            if s > curEnd:
                arrows += 1
                curEnd = e
        return arrows