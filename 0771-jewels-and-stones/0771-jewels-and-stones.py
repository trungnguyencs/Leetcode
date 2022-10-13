class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([ch in jewels for ch in stones])