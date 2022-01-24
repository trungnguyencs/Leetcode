class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target) for _ in range(d)]
        for c in range(min(f, target)):
            dp[0][c] = 1
        for r in range(1, d):
            for c in range(target):
                for i in range(1, f + 1):
                    if c >= i:
                        dp[r][c] += dp[r-1][c-i]
        return dp[-1][-1] % (10**9 + 7)
