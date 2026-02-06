class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i, num in enumerate(nums):
            j = bisect.bisect_right(nums, num * k)
            ans = min(ans, i + (len(nums) - j))
        return ans