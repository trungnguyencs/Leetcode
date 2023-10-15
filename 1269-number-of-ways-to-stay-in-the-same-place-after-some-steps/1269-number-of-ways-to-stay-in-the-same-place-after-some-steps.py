class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(steps, i):
            if i in (-1, arrLen): return 0
            if i > steps: return 0
            if i == steps: return 1
            return (dp(steps - 1, i - 1) + dp(steps - 1, i) + dp(steps - 1, i + 1)) % MOD
        
        return dp(steps, 0)