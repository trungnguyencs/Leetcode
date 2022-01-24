class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        r, g, b = costs[0]
        for row in range(1, len(costs)):
            r, g, b = costs[row][0] + min(g, b), costs[row][1] + min(r, b), costs[row][2] + min(r, g)
        return min(r, g, b)