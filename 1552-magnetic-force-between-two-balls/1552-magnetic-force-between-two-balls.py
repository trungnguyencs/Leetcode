class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 1, position[-1] - position[0]
        while lo <= hi:
            mid = (lo + hi)//2
            if not self.canPlaceMBalls(position, m, mid):
                hi = mid - 1
            elif not self.canPlaceMBalls(position, m, mid + 1):
                return mid
            else:
                lo = mid + 1
        
    def canPlaceMBalls(self, position, m, d):
        count = 1
        prev = position[0]
        for i in range(1, len(position)):
            if position[i] - prev >= d:
                count += 1
                prev = position[i]
            if count >= m: return True
        return False