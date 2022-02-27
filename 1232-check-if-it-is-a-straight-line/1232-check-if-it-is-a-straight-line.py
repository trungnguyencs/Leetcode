class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        for x, y in coordinates[2:]:
            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0): return False
        return True