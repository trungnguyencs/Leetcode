class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedUniques = sorted(set(arr))
        ranks = {num: i + 1 for i, num in enumerate(sortedUniques)}
        return [ranks[num] for num in arr]