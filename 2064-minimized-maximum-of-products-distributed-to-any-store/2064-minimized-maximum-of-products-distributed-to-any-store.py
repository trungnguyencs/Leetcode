class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        while l <= r:
            m = (l + r)//2
            if self.minStoreRequired(quantities, m) > n:
                l = m + 1
            else:
                r = m - 1
        return l
        
    def minStoreRequired(self, quantities, x):
        stores = sum(ceil(q/x) for q in quantities)
        return stores