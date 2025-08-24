class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # same as longest window with at most one 0
        longest = l = zeroCount = 0
        for r, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
                while zeroCount == 2:
                    if nums[l] == 0:
                        zeroCount -= 1
                    l += 1
            longest = max(longest, r - l + 1)
        return longest - 1       