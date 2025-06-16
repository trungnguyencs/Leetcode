class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curMin = nums[0]
        ans = -1
        for i in range(1, len(nums)):
            if nums[i] > curMin:
                ans = max(ans, nums[i] - curMin)
            elif nums[i] < curMin:
                curMin = nums[i]
        return ans