class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            maxSum = max(maxSum, cur)
        return maxSum