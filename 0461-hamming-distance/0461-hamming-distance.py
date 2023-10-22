class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        while x or y:
            d += (x & 1 != y & 1)
            x >>= 1
            y >>= 1
        return d