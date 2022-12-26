class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, num in enumerate(nums):
            if maxReach < i: return False
            maxReach = max(maxReach, i + num)
        return True