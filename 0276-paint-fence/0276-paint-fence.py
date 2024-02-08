class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2: return k*k
        same, diff = k, k*(k - 1)
        for _ in range (3, n + 1):
            same, diff = diff, (same + diff)*(k - 1)
        return same + diff