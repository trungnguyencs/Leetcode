class Solution:
    def maxLength(self, ribbons: List[int], K: int) -> int:
        if sum(ribbons) < K: return 0
        l, r = 1, max(ribbons)
        while l <= r:
            m = (l + r)//2
            k = self.countSections(ribbons, m)
            if k >= K and self.countSections(ribbons, m + 1) < K:
                return m
            if k < K:
                r = m - 1
            else:
                l = m + 1
            
    def countSections(self, ribbons, length):
        return sum(ribbon//length for ribbon in ribbons)