class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = self.findFirstDecreasingFromBack(nums)
        if i == -1:
            self.reverse(nums, 0)
            return
        j = self.findFirstLargerFromBack(nums, nums[i])
        nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1)
            
    def findFirstDecreasingFromBack(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                return i - 1
        return -1
        
    def findFirstLargerFromBack(self, nums, target):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > target:
                break
        return i
        
    def reverse(self, nums, i):
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -=1