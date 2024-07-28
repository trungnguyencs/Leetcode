class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = maxStreak = 0
        for num in nums:
            if num == 1:
                streak += 1
                maxStreak = max(maxStreak, streak)
            else:
                streak = 0
        return maxStreak