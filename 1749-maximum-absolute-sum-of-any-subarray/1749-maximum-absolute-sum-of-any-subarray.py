class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #max absolute sum is max(maxSum, -minSum)
        maxSum = self.findMaxSum(nums)
        minSum = self.findMinSum(nums)
        return max(maxSum, abs(minSum))

    def findMaxSum(self, nums):
        cur = maxSum = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            maxSum = max(maxSum, cur)
        return maxSum

    def findMinSum(self, nums):
        cur = minSum = nums[0]
        for i in range(1, len(nums)):
            cur = min(cur + nums[i], nums[i])
            minSum = min(minSum, cur)
        return minSum