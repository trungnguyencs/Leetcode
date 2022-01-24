class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = streak = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                streak += 1
                ans += streak
            else:
                streak = 0
        return ans