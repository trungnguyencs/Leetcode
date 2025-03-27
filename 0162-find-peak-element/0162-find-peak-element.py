class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n - 1
        l, r = 1, n - 2
        while l <= r:
            m = (l + r)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            if nums[m] > nums[m-1]:
                l = m + 1
            else:
                r = m - 1