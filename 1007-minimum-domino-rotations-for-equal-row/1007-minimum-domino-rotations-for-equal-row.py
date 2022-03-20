class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = min(self.helper(tops, bottoms), self.helper(bottoms, tops))
        return -1 if ans == float('inf') else ans
        
    def helper(self, tops, bottoms):
        counter = Counter(tops)
        mostPopular = max(counter.keys(), key=lambda x: counter[x])
        flip = 0
        for i in range(len(tops)):
            if mostPopular not in [tops[i], bottoms[i]]:
                return float('inf')
            if tops[i] != mostPopular:
                flip += 1
        return flip