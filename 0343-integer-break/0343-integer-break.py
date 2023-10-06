class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n == 1: return 1
            return max(n, max(dp(n - i)*i for i in range(1, n)))
        
        return max(dp(n - i)*i for i in range(1, n))