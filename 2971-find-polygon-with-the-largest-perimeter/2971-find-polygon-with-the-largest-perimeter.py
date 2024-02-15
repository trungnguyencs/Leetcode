class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        curSum, totalSum = 0, sum(nums)
        for i in range(len(nums) - 1):
            curSum += nums[i]
            if nums[i] < totalSum - curSum:
                return totalSum - (curSum - nums[i])
        return -1