class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1] + 1)
        for d in range(1, days[-1] + 1):
            if d not in days:
                dp[d] = dp[d-1]
            else:
                dp[d] = min(dp[d-1] + costs[0], dp[max(0, d-7)] + costs[1], dp[max(0, d-30)] + costs[2])
        return dp[-1]