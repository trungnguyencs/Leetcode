class Solution:
    def bulbSwitch(self, n: int) -> int:
        # square numbers will be toggled odd times -> will be on
        return int(n**0.5)