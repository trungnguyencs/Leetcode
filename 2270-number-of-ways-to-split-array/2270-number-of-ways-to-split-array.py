class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = left = 0
        total = sum(nums)
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left: count += 1
        return count