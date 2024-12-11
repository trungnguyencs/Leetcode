class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        maxLen = 0
        for r, num in enumerate(nums):
            while num - k > nums[l] + k:
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen