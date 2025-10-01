class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = empty = numBottles
        while empty >= numExchange:
            div, mod = divmod(empty, numExchange)
            drank += div
            empty = div + mod
        return drank