class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.bisectLeft(nums, target), self.bisectRight(nums, target)]
    
    def bisectLeft(self, nums, target):
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                ans = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return ans
            
    def bisectRight(self, nums, target):
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                ans = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return ans