class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = self.findLeftMostIndex(nums, target)
        if left == -1: return False
        right = left + len(nums)//2
        return right < len(nums) and nums[right] == target
        
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