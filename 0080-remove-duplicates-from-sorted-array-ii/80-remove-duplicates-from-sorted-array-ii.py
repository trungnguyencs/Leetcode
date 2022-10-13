class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        while r < len(nums):
            k = 2
            cur = nums[r]
            # iterate through all identical elements
            while r < len(nums) and nums[r] == cur:
                if k > 0:
                    nums[l] = nums[r]
                    l += 1
                    k -= 1
                r += 1
        return l