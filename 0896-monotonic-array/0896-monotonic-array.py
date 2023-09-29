class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        isIncreasing = nums[0] <= nums[-1]
        return all((nums[i] <= nums[i+1] and isIncreasing) or (nums[i] >= nums[i+1] and not isIncreasing) for i in range(len(nums) - 1))