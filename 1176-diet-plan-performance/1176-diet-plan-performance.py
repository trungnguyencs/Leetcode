class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pts = cur = 0
        for i in range(len(calories)):
            cur += calories[i]
            if i >= k:
                cur -= calories[i-k]
            if i >= k - 1:
                d = -1 if cur < lower else 1 if cur > upper else 0
                pts += d
        return pts