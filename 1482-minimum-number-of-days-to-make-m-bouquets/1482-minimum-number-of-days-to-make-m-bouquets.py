class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        lo, hi = 1, max(bloomDay)
        while lo <= hi:
            mid = (lo + hi)//2
            if not self.isSatisfactory(bloomDay, m, k, mid):
                lo = mid + 1
            elif not self.isSatisfactory(bloomDay, m, k, mid - 1):
                return mid
            else:
                hi = mid - 1
        return -1
        
    def isSatisfactory(self, bloomDay, m, k, d):
        streak = count = 0
        for num in bloomDay:
            if num <= d:
                streak += 1
                if streak == k:
                    streak = 0
                    count += 1
            else:
                streak = 0
        return count >= m