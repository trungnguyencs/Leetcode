class Solution:
    def numDecodings(self, s: str) -> int:
        dic = defaultdict(int)
        dic.update({str(one): 1 for one in range (1, 10)})
        dic.update({str(two): 1 for two in range(10, 27)})
        dp = 1, dic[s[:1]]
        for i in range(1, len(s)):
            dp = dp[1], dp[1]*dic[s[i]] + dp[0]*dic[s[i-1:i+1]]
        return dp[1]