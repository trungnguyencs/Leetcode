class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = ans = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0:
                inc += 1
                dec = 1
            elif diff < 0:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)
        return ans