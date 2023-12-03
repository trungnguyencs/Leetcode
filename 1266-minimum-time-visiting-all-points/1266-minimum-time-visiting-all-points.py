class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(self.minTimeTravel(points[i], points[i+1]) for i in range(len(points) - 1))
        
    def minTimeTravel(self, ptA, ptB):
        dx, dy = abs(ptA[0] - ptB[0]), abs(ptA[1] - ptB[1])
        return max(dx, dy)