class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ownStock = -prices[0]
        cooldown = float('-inf')
        free = 0
        for price in prices[1:]:
            ownStock, cooldown, free = max(ownStock, free - price), ownStock + price, max(free, cooldown)
        return max(free, cooldown)