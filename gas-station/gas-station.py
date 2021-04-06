class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, have, owe = -1, 0, 0
        for i in range(len(gas)):
            have += gas[i] - cost[i]
            if have < 0:
                owe -= have
                have = 0
                start = -1
            elif start == -1: start = i
        return start if have >= owe else -1