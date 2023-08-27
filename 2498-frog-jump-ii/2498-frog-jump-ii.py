class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2: return stones[1] - stones[0]
        return max(stones[i+2] - stones[i] for i in range(len(stones) - 2))