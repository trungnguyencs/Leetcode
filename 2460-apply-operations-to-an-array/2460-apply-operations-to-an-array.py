class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                continue
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                nums[left] = nums[i] * 2
                nums[i+1] = 0
            else:
                nums[left] = nums[i]
            left += 1
        for j in range(len(nums) - 1, len(nums) - zeroCount - 1, -1):
            nums[j] = 0
        return nums