class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # totalDistance = 2*(sum(d_nut_tree)) + d_firstNut_squirrel - d_firstNut_tree
        # so choose nut that minimize d_firstNut_squirrel - d_firstNut_tree
        nuts2Tree = 0
        minDelta = float('inf')
        for nut in nuts:
            d = self.getDistance(nut, tree)
            nuts2Tree += d
            minDelta = min(minDelta, self.getDistance(squirrel, nut) - d)
        return 2*nuts2Tree + minDelta
        
    def getDistance(self, ptA, ptB):
        return abs(ptA[0] - ptB[0]) + abs(ptA[1] - ptB[1])