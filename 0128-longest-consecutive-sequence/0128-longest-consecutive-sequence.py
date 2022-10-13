class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        maxStreak = 0
        for num in nums:
            if num - 1 in uniq: continue
            streak = 1
            while num + 1 in uniq:
                streak += 1
                num += 1
            maxStreak = max(maxStreak, streak)
        return maxStreak