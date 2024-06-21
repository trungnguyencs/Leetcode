class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], m: int) -> int:
        satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        window = maxWindow = sum(customers[i]*grumpy[i] for i in range(m))
        for i in range(m, len(customers)):
            window += customers[i] * grumpy[i] - customers[i-m] * grumpy[i-m]
            maxWindow = max(maxWindow, window)
        return satisfied + maxWindow