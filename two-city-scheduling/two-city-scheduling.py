class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        totalCost = 0
        for i in range(len(costs)//2):
            totalCost += costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            totalCost += costs[i][1]
        return totalCost