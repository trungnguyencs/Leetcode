class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.backtrack(nums, 0, 0)

    def backtrack(self, nums, i, xor):
        if i == len(nums):
            return xor
        return self.backtrack(nums, i + 1, xor ^ nums[i]) + self.backtrack(nums, i + 1, xor)