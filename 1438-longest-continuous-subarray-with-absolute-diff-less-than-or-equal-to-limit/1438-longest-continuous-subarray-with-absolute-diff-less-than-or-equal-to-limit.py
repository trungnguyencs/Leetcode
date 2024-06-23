from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        slidingWindow = SortedList()
        l = maxWindow = 0
        for r, num in enumerate(nums):
            slidingWindow.add(num)
            while slidingWindow[-1] - slidingWindow[0] > limit:
                slidingWindow.remove(nums[l])
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow