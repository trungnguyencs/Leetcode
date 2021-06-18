class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prevIncrease = False
        for i in range(len(nums)-1):
            if (nums[i+1] > nums[i] and prevIncrease) or (nums[i+1] < nums[i] and not prevIncrease):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            prevIncrease = not prevIncrease