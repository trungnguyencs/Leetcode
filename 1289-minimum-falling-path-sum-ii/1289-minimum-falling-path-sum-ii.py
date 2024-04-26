class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[0]
        for r in range(1, n):
            newDp = [float('inf')]*n
            for c1 in range(n):
                for c2 in range(n):
                    if c1 == c2: continue
                    newDp[c1] = min(newDp[c1], grid[r][c1] + dp[c2])
            dp = newDp
        return min(dp)