class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # O(n) space
        dp = [0]*len(grid[0])
        dp[0] = grid[0][0]
        for c in range(1, len(grid[0])):
            dp[c] = dp[c-1] + grid[0][c]
        for r in range(1, len(grid)):
            dp[0] += grid[r][0]
            for c in range(1, len(grid[0])):
                dp[c] = grid[r][c] + min(dp[c], dp[c-1])
        return dp[-1]