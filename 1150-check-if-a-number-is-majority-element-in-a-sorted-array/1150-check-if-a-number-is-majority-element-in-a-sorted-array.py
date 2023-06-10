class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = self.findLeftMostIndex(nums, target)
        right = self.findRightMostIndex(nums, target)
        if -1 in [left, right]: return False
        return right - left + 1 > len(nums)//2
        
    def findLeftMostIndex(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif m > 0 and nums[m-1] == target:
                r = m - 1
            else:
                return m
        return -1
    
    def findRightMostIndex(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif m < len(nums) - 1 and nums[m+1] == target:
                l = m + 1
            else:
                return m
        return -1