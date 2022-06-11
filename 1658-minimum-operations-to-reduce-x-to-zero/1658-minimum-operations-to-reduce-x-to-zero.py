class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x # find max window that sums to target
        if target < 0: return -1
        maxLen, l, s = -1, 0, 0
        for r, num in enumerate(nums):
            s += num
            while s > target:
                s -= nums[l]
                l += 1
            if s == target:
                maxLen = max(maxLen, r - l + 1)
        return -1 if maxLen == -1 else len(nums) - maxLen