class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay, maxProfit = float('inf'), 0
        for price in prices:
            maxProfit = max(maxProfit, price - minDay)
            minDay = min(minDay, price)
        return maxProfit
