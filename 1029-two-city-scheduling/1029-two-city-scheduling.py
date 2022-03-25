class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        minCost = 0
        for i, (costA, costB) in enumerate(costs):
            minCost += costA if i < len(costs)//2 else costB
        return minCost