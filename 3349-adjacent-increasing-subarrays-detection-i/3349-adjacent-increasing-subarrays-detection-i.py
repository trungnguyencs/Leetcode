class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        #split nums into adjacent monotonic increasing arrays
        prevStreak = 0
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                streak += 1
            else:
                prevStreak = streak
                streak = 1
            if streak >= 2 * k or (prevStreak >= k and streak >= k):
                return True
        return False