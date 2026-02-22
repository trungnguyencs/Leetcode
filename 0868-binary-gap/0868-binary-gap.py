class Solution:
    def binaryGap(self, n: int) -> int:
        distance = maxDistance = float('-inf')
        while n:
            b = n & 1
            if b == 0:
                distance += 1
            else:
                maxDistance = max(maxDistance, distance)
                distance = 0
            n >>= 1
        return 0 if maxDistance == float('-inf') else maxDistance + 1