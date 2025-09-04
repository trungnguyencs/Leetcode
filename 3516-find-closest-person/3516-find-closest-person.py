class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x - z), abs(y - z)
        return 1 if d1 < d2 else 2 if d1 > d2 else 0