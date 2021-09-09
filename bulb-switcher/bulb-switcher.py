class Solution:
    def bulbSwitch(self, n: int) -> int:
        # only bulbs whose index is a perfect square will be on
        return int(n ** 0.5)