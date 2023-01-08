class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        ans = 1
        for i in range(len(points) - 1):
            counter = Counter()
            for j in range(i + 1, len(points)):
                slope = self.findSlope(points[i], points[j])
                counter[slope] += 1
                ans = max(ans, 1 + counter[slope])
        return ans
        
    def findSlope(self, p1, p2):
        if p1[0] == p2[0]: return float('inf')
        return (p2[1] - p1[1])/(p2[0] - p1[0])