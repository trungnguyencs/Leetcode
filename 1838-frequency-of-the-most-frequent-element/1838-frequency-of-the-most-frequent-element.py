class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # longest window such that k + sum(window from l to r) >= nums[r] * (r - l + 1)
        nums.sort()
        l = s = maxWindow = 0
        for r, num in enumerate(nums):
            s += num
            while s + k < num * (r - l + 1):
                s -= nums[l]
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow