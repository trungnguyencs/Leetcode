class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        avail = sorted([capacity[i] - rocks[i] for i in range(len(capacity))])
        count = 0
        for i in range(len(capacity)):
            if avail[i] > additionalRocks: break
            count += 1
            additionalRocks -= avail[i]
        return count