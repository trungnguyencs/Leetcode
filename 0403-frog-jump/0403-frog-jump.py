class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp[i][j]: can frog make a step of size j from stones[i]
        N = len(stones)
        dp = [[False]*N for _ in range(N)]
        dp[0][1] = True
        for i in range(N):
            for j in range(i + 1, N):
                d = stones[j] - stones[i]
                if 0 < d < N and dp[i][d]:
                    if j == N - 1: return True
                    dp[j][d] = True
                    if d > 0: dp[j][d-1] = True
                    if d < N: dp[j][d+1] = True
        return False