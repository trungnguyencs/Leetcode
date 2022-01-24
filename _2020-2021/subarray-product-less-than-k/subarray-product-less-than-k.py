class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod, count = 1, 0
        l = 0
        for r, num in enumerate(nums):
            prod *= num
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            count += r - l + 1
        return count