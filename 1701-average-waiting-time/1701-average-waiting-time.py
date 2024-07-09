class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWaitTime = curTime = 0
        for customerTime, prepTime in customers:
            curTime = max(curTime, customerTime) + prepTime
            totalWaitTime += curTime - customerTime
        return totalWaitTime/len(customers)