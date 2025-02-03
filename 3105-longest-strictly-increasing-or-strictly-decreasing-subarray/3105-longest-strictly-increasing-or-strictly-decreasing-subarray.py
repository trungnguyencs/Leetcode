class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        lastDiff = 0
        streak = maxStreak = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 0:
                streak = 1
            elif diff * lastDiff < 0:
                streak = 2
            else:
                streak += 1
            maxStreak = max(maxStreak, streak)
            lastDiff = diff
        return maxStreak