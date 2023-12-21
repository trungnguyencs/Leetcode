class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xCoordinates = sorted(list(set(p[0] for p in points)))
        return 0 if len(xCoordinates) == 1 else max(xCoordinates[i+1] - xCoordinates[i] for i in range(len(xCoordinates) - 1))