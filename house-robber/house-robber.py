class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        prev, cur = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            prev, cur = cur, max(cur, prev + num)
        return cur