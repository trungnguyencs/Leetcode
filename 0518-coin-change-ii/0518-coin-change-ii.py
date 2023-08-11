class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # if not amount: return 1
        # dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        # for r in range(1, len(coins)+1):
        #     dp[r][0] = 1
        # for r in range(1, len(coins)+1):
        #     for c in range(1, amount+1):
        #         if c < coins[r-1]:
        #             dp[r][c] = dp[r-1][c]
        #         else:
        #             dp[r][c] = dp[r-1][c] + dp[r][c-coins[r-1]]
        # return dp[-1][-1]
        
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(len(dp)):
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[-1]