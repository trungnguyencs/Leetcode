class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: return 0
        l, r = 1, max(candies)
        while l <= r:
            m = (l + r)//2
            isSatisfied = self.canGetKChildren(candies, m, k)
            if not isSatisfied:
                r = m - 1
            elif not self.canGetKChildren(candies, m + 1, k):
                return m
            else:
                l = m + 1
    
    def canGetKChildren(self, candies, lot, k):
        return sum(c//lot for c in candies) >= k