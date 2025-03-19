class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                ops += 1
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
        return ops if nums[-1] == nums[-2] == 1 else -1