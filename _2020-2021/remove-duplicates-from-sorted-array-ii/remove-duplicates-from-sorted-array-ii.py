class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for num in nums:
            if l < 2 or nums[l-2] != num:
                nums[l] = num
                l += 1
        return l