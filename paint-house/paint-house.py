class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for r in range(1, len(costs)):
            costs[r][0] += min(costs[r-1][1], costs[r-1][2])
            costs[r][1] += min(costs[r-1][0], costs[r-1][2])
            costs[r][2] += min(costs[r-1][0], costs[r-1][1])
        return min(costs[-1])