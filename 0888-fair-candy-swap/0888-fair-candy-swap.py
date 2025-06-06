class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = sum(bobSizes) - sum(aliceSizes)
        bSet = set(bobSizes)
        for a in aliceSizes:
            if a + diff/2 in bSet:
                return [a, a + diff//2]