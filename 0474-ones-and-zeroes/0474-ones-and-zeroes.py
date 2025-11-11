class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [(s.count('0'), s.count('1')) for s in strs]

        @cache
        def dp(i, mm, nn):
            if mm < 0 or nn < 0: return float('-inf')
            if i == len(strs): return 0
            x, y = xy[i]
            return max(dp(i + 1, mm, nn), 1 + dp(i + 1, mm - x, nn - y))

        return dp(0, m, n)