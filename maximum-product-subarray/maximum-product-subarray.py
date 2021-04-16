class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = globalMax = nums[0]
        for num in nums[1:]:
            prevMax, prevMin = curMax, curMin
            curMax = max(num, prevMax*num, prevMin*num)
            curMin = min(num, prevMin*num, prevMax*num)
            globalMax = max(globalMax, curMax)
        return globalMax