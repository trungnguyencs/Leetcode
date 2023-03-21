class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = streak = 0
        for num in nums:
            if num == 0:
                streak += 1
                ans += streak
            else:
                streak = 0
        return ans