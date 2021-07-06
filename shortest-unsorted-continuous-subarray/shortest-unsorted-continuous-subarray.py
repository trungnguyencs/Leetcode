class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i, j = self.findFirstOutOfOrder(nums), self.findLastOutOfOrder(nums)
        if -1 in [i, j]: return 0 # already sorted
        m, M = min(nums[i:j+1]), max(nums[i:j+1])
        while i >= 0 and nums[i] > m:
            i -= 1
        while j < len(nums) and nums[j] < M:
            j += 1
        return j - i - 1
        
    def findFirstOutOfOrder(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: return i
        return -1
    
    def findLastOutOfOrder(self, nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]: return i
        return -1