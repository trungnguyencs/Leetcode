class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n + 1
        while l < r:
            m = (l + r)//2
            S, nextS = self.sumTo(m), self.sumTo(m+1)
            if S <= n < nextS: return m
            if S < n:
                l = m + 1
            else:
                r = m
        
    def sumTo(self, n):
        return n*(n+1)//2