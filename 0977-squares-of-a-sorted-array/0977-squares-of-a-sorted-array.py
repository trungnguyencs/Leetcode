class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        ans = [0]*len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l]**2
                l += 1
            else:
                ans[i] = nums[r]**2
                r -= 1
            i -= 1
        return ans