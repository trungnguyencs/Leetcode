class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = time % (n * 2 - 2)
        if mod < n: return mod + 1
        return n - (mod - (n - 1))