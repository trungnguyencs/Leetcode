class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = max(nums)
        streak = maxStreak = 0
        for r, num in enumerate(nums):
            if num == maxNum:
                streak += 1
                maxStreak = max(maxStreak, streak)
            else:
                streak = 0
        return maxStreak       