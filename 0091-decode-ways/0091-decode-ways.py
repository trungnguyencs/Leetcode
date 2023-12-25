class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0]*(len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(1, len(s)):
            j = i + 1
            if s[i] != '0':
                dp[j] = dp[j-1]
            elif s[i-1] not in '12':
                return 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] in '0123456'):
                dp[j] += dp[j-2]
        return dp[-1]