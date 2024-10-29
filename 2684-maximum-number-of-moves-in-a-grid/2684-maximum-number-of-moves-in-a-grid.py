class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [1]*R
        ans = 0
        for c in range(1, C):
            newDp = [0]*R
            for r in range(R):
                left = 1 + dp[r-1] if 0 <= r-1 < R and dp[r-1] > 0 and grid[r][c] > grid[r-1][c-1] else 0 
                mid = 1 + dp[r] if dp[r] > 0 and grid[r][c] > grid[r][c-1] else 0
                right = 1 + dp[r+1] if 0 <= r+1 < R and dp[r+1] > 0 and grid[r][c] > grid[r+1][c-1] else 0
                newDp[r] = max(left, mid, right)
                ans = max(ans, newDp[r] - 1)
            dp = newDp
        return ans