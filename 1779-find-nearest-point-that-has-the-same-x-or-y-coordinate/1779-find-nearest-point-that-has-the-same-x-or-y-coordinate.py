class Solution:
    def nearestValidPoint(self, x0: int, y0: int, points: List[List[int]]) -> int:
        ans = -1
        minDiff = float('inf')
        for i, (x, y) in enumerate(points):
            if (x == x0 or y == y0) and abs(x - x0) + abs(y - y0) < minDiff:
                minDiff = abs(x - x0) + abs(y - y0)
                ans = i
        return ans