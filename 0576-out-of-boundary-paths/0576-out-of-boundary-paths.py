class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(r, c, move):
            if move < 0: return 0
            if not (0 <= r < m and 0 <= c < n): return 1
            return (dp(r - 1, c, move - 1)\
                    + dp(r + 1, c, move - 1)\
                    + dp(r, c - 1, move - 1)\
                    + dp(r, c + 1, move - 1)) % MOD
        return dp(startRow, startColumn, maxMove)