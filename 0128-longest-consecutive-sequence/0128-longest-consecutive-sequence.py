class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxStreak = 0
        for num in numSet:
            if num - 1 in numSet: continue
            streak = 1
            while num + 1 in numSet:
                num += 1
                streak += 1
            maxStreak = max(maxStreak, streak)
        return maxStreak