class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxSum = -1
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                l += 1
                maxSum = max(maxSum, s)
            else:
                r -= 1
        return maxSum