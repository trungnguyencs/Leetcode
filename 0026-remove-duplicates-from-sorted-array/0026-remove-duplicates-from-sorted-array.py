class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r, num in enumerate(nums):
            if num != nums[l]:
                l += 1
                nums[l] = num
        return l + 1