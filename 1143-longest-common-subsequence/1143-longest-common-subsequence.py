class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s2) + 1) for _ in range(len(s1) + 1)]
        for r in range(1, len(s1) + 1):
            for c in range(1, len(s2) + 1):
                dp[r][c] = 1 + dp[r-1][c-1] if s1[r-1] == s2[c-1] else max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]