class Solution:
    def shipWithinDays(self, weights: List[int], k: int) -> int:
        l, r = 1, sum(weights)
        while l <= r:
            m = (l + r)//2
            if self.canShipWithinKDays(weights, k, m):
                if not self.canShipWithinKDays(weights, k, m-1):
                    return m
                r = m - 1
            else:
                l = m + 1
        
    def canShipWithinKDays(self, weights, k, capacity):
        if max(weights) > capacity: return False
        ships, cur = 1, capacity
        for w in weights:
            if cur >= w:
                cur -= w
            else:
                ships += 1
                cur = capacity - w
        return ships <= k