class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = min(self.helper(tops, bottoms), self.helper(bottoms, tops))
        return -1 if ans == float('inf') else ans
        
    def helper(self, tops, bottoms):
        topCount = bottomCount = 0
        base = tops[0]
        for i in range(len(tops)):
            if base not in [tops[i], bottoms[i]]:
                return float('inf')
            if tops[i] == base:
                topCount += 1
            if bottoms[i] == base:
                bottomCount += 1
        return min(len(tops) - topCount, len(tops) - bottomCount)