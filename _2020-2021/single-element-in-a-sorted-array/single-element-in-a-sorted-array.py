class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] not in [nums[m-1], nums[m+1]]: return nums[m]
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m - 1  