class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(n, target):
            if target < n: return 0
            if n == 0: return 0
            if n == 1 and target <= k: return 1
            return sum(dp(n - 1, target - i) for i in range(1, k + 1)) % MOD
                       
        return dp(n, target)