class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[-1] == math.inf else dp[-1] 