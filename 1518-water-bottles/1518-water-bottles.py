class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            div, mod = divmod(numBottles, numExchange)
            ans += div
            numBottles = div + mod
        return ans