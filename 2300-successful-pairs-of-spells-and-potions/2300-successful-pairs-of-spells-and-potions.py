class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            target = success/spell
            i = bisect_left(potions, target)
            ans.append(len(potions) - i)
        return ans