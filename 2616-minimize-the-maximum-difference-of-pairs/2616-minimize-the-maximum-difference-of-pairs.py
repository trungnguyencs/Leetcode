class Solution:
    def minimizeMax(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            m = (l + r)//2
            if self.canFindKPairs(m, nums, k):
                r = m - 1
            else:
                l = m + 1
        return l
    
    def canFindKPairs(self, d, nums, k):
        i, count = 1, 0
        while i < len(nums):
            if nums[i] - nums[i-1] <= d:
                count += 1
                i += 1
            i += 1
        return count >= k