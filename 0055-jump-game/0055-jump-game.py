class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp will take O(n^2)
        #greedy O(n): use a variable maxReach to find out if there's an index that cannot be reached
        maxReach = 0
        for i, num in enumerate(nums):
            if maxReach < i: return False
            maxReach = max(maxReach, i + num)
        return True