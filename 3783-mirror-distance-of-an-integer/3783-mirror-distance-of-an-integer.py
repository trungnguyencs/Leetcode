class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror, N = 0, n
        while N:
            d = N % 10
            mirror = mirror * 10 + d
            N //= 10
        return abs(mirror - n)