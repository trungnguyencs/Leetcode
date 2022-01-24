class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                # from tail, find the first decreasing pairs (i, i+1)
                for j in range(len(nums)-1, i, -1):
                    # from tail -> i+1, find the first smallest number > nums[i] and swap them
                    # as the tail is still in decreasing order, reverse it to get the smallest tail
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        self.reverse(nums, i+1)
                        return
        self.reverse(nums, 0)
        
    def reverse(self, nums, i):
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1