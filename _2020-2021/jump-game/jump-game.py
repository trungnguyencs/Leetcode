class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthestReachable = 0
        for i, maxStep in enumerate(nums):
            if furthestReachable >= len(nums)-1: break
            if furthestReachable < i: return False
            furthestReachable = max(furthestReachable, i + maxStep)
        return True