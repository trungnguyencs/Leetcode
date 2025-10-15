class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        prevStreak = 0
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                streak += 1
            else:
                prevStreak = streak
                streak = 1
            ans = max(ans, min(prevStreak, streak), streak//2)
        return ans