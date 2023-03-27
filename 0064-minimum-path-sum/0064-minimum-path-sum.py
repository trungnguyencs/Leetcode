class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[0].copy()
        for i in range(1, len(dp)):
            dp[i] += dp[i-1]
        for r in range(1, len(grid)):
            dp[0] += grid[r][0]
            for c in range(1, len(dp)):
                dp[c] = grid[r][c] + min(dp[c], dp[c-1])
        return dp[-1]