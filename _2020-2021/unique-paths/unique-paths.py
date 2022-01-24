class Solution:
    def uniquePaths(self, m: int, n: int) -> int:       
        # O(n) space:
        dp = [1]*n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c-1]
        return dp[-1]