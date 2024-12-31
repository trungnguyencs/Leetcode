class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayPass, weekPass, monthPass = costs
        dp = [0]*(days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + dayPass,
                            dp[max(0, i-7)] + weekPass,
                            dp[max(0, i-30)] + monthPass)
        return dp[-1]