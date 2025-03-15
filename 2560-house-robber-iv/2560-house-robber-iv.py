class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r)//2
            if not self.canGetKHouses(nums, k, m):
                l = m + 1
            elif not self.canGetKHouses(nums, k, m - 1):
                return m
            else:
                r = m - 1

    def canGetKHouses(self, nums, k, maxCap):
        i = 0
        houses = 0
        while i < len(nums):
            if nums[i] <= maxCap:
                houses += 1
                i += 2
                if houses >= k: return True
            else:
                i += 1
        return False