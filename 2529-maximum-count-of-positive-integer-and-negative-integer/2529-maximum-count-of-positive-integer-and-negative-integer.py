class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negativeCount = bisect_left(nums, 0)
        positiveCount = len(nums) - bisect_right(nums, 0)
        return max(negativeCount, positiveCount)