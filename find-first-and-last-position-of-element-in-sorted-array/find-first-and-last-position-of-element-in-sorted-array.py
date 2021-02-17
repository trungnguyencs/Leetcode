class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.bisectLeft(nums, target), self.bisectRight(nums, target)]
        
    # l in bisectLeft is the left most index to insert target
    def bisectLeft(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r)//2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l if 0 <= l < len(nums) and nums[l] == target else -1
    
    # l in bisectRight is the right most index to insert target
    def bisectRight(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r)//2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        return l-1 if 0 < l < len(nums)+1 and nums[l-1] == target else -1