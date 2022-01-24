class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        return max(self.robNonCircular(nums[1:]), self.robNonCircular(nums[:-1]))
        
    def robNonCircular(self, nums):
        prev, cur = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev, cur = cur, max(cur, nums[i] + prev)
        return cur