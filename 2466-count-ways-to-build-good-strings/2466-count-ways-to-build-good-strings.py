class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        return (self.helper(high, zero, one) - self.helper(low - 1, zero, one)) % (10**9 + 7)

    def helper(self, limit, zero, one):
        #dp[i]: number of strings that have length i
        dp = [0]*(limit + 1)
        dp[0] = 1
        for i in range(limit + 1):
            if i + zero <= limit:
                dp[i + zero] += dp[i]
            if i + one <= limit:
                dp[i + one] += dp[i]
        return sum(dp)