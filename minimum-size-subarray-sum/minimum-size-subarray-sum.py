class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans, sum = float('inf'), 0
        l = 0
        for r, num in enumerate(nums):
            sum += nums[r]
            while sum >= s:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0
