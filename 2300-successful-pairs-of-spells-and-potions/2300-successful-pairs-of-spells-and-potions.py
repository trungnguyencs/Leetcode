class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        return [n - bisect_left(potions, success/spell) for spell in spells]