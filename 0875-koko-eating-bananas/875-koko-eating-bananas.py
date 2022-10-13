class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            m = (lo + hi)//2
            hours = sum(p//m if p % m == 0 else p//m + 1 for p in piles)
            if hours > h:
                lo = m + 1
            else:
                hi = m - 1
        return lo