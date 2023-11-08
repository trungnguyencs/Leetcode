class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(sx - fx), abs(sy - fy)
        if dx > t or dy > t or (dx == dy == 0 and t == 1):
            return False
        return True