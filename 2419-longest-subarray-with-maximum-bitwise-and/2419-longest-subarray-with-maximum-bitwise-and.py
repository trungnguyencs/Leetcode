class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #maxBitWiseAND = max(nums)
        maxNum = max(nums)
        streak = maxStreak = 0
        for num in nums:
            if num == maxNum:
                streak += 1
                maxStreak = max(maxStreak, streak)
            else:
                streak = 0
        return maxStreak