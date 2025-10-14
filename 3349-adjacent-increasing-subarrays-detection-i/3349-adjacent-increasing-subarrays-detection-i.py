class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 2 * k + 1):
            if self.isStrictlyIncreasing(nums, i, k) and self.isStrictlyIncreasing(nums, i + k, k):
                return True
        return False

    def isStrictlyIncreasing(self, nums, i, k):
        if k == 1: return True
        return all(nums[j] < nums[j+1] for j in range(i, i + k - 1))