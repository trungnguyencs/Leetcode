class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = float('inf')
        maxProfit = 0
        for p in prices:
            maxProfit = max(maxProfit, p - minCost)
            minCost = min(minCost, p)
        return maxProfit