class Solution:
    @cache
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        if high < min(zero, one): return 0        
        ans = 0
        if high >= zero:
            if low <= zero: ans += 1
            ans += self.countGoodStrings(low - zero, high - zero, zero, one)
        if high >= one:
            if low <= one: ans += 1
            ans += self.countGoodStrings(low - one, high - one, zero, one)
        return ans % (10**9 + 7)