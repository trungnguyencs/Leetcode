class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # # Memory limit exceeded?
        # counter = Counter(s)
        # ans = 0
        # @cache
        # def dp(i, n):
        #     if n == 0: return 1
        #     if i == 25:
        #         return dp(0, n - 1) + dp(1, n - 1)
        #     return dp(i + 1, n - 1)
        # for ch, freq in counter.items():
        #     ans += freq * dp(ord(ch) - ord('a'), t)
        # return ans % (10**9 + 7)
        counter = Counter(s)
        ans = 0
        dp = deque([1] * 26)
        for _ in range(t):
            dp.append(dp[0] + dp[1]) #dp[i][z] = dp[i-1][a] + dp[i-1][b]
            dp.popleft()
        for ch, freq in counter.items():
            i = ord(ch) - ord('a')
            ans += freq * dp[i]
        return ans % (10**9 + 7)