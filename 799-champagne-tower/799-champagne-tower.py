class Solution:
    def champagneTower(self, amount: int, query_row: int, query_glass: int) -> float:
        dp = [amount]
        for _ in range(query_row):
            newDp = [0]*(len(dp) + 1)
            for i in range(len(dp)):
                overflow = max(0, dp[i] - 1)
                newDp[i] += overflow/2
                newDp[i+1] += overflow/2
            dp = newDp
        return min(1, dp[query_glass])