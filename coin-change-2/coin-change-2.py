class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # recurrence: dp[r][c] = dp[r-1][c] + dp[r][c - coin]
        dp = [0]*(amount + 1)
        dp[0] = 1
        for r, coin in enumerate(coins):
            for c in range(1, amount + 1):
                if c < coin: continue
                dp[c] += dp[c - coin]     
        return dp[-1]