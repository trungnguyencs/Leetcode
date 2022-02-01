class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit