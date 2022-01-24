class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return 0
        dp = [1 for _ in range(len(grid[0]))]
        for c in range(1, len(grid[0])):
            dp[c] = 0 if grid[0][c] else dp[c-1]
        for r in range(1, len(grid)):
            if grid[r][0]: dp[0] = 0
            for c in range(1, len(grid[0])):
                dp[c] = 0 if grid[r][c] else dp[c-1] + dp[c]
        return dp[-1]