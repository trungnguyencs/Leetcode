class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        maxDiffHorizontal = max([horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1)])
        maxDiffVertical = max([verticalCuts[i+1] - verticalCuts[i] for i in range(len(verticalCuts) - 1)])
        return (maxDiffHorizontal*maxDiffVertical) % (10**9 + 7)