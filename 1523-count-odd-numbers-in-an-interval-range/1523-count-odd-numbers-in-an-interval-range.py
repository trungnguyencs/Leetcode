class Solution:
    def countOdds(self, low: int, high: int) -> int:
        half = (high - low)//2
        return half if low % 2 == high % 2 == 0 else half + 1