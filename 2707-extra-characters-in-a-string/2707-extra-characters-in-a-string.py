class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dic = set(dictionary)
        dp = [float('inf')]*(len(s) + 1)
        dp[0] = 0
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in dic:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)
        return dp[-1]