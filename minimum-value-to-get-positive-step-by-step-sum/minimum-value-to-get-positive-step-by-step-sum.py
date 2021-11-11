class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minCumulative, cumulative = math.inf, 0
        for num in nums:
            cumulative += num
            minCumulative = min(minCumulative, cumulative)
        return max(1, 1 - minCumulative)