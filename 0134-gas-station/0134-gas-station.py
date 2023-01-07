class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        have = own = ans = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            if have < 0:
                own -= have
                have = 0
                ans = i
            have += g - c
        return ans if have >= own else -1