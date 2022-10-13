class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        R, C = len(word1), len(word2)
        dp = [[0]*(C + 1) for _ in range(R + 1)]
        for r in range(R + 1):
            dp[r][0] = r
        for c in range(C + 1):
            dp[0][c] = c
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                dp[r][c] = dp[r-1][c-1] if word1[r-1] == word2[c-1] else 1 + min(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]