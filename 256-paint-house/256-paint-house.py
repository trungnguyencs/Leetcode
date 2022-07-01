class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            tmp = [0]*3
            tmp[0] = costs[i][0] + min(dp[1], dp[2])
            tmp[1] = costs[i][1] + min(dp[0], dp[2])
            tmp[2] = costs[i][2] + min(dp[0], dp[1])
            dp = tmp
        return min(dp)