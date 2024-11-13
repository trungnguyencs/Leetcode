import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for i, num in enumerate(nums):
            lowerBound = lower - num
            upperBound = upper - num
            l = bisect_left(nums, lowerBound, lo=i+1)
            r = bisect_right(nums, upperBound, lo=i+1)
            ans += max(0, r - l)
        return ans