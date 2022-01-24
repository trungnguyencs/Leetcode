class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for num in s:
            if num - 1 in s: continue
            streak = 1
            while num + 1 in s:
                num += 1
                streak += 1
            maxLen = max(maxLen, streak)
        return maxLen           