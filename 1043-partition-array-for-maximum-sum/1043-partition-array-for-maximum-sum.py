class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # dp[i]: maxSum at A[i-1]
        n = len(A)
        dp = [0]*(n + 1)
        for i in range(1, n + 1):
            curMax = 0
            for k in range(1, min(K, i) + 1):
                curMax = max(curMax, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[-1]