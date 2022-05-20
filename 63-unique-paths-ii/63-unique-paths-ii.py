class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0
        dp = [0]*len(grid[0])
        dp[0] = 1
        for row in grid:
            for i in range(len(dp)):
                if row[i] == 1:
                    dp[i] = 0
                else:
                    dp[i] += 0 if i == 0 else dp[i-1]
        return dp[-1]