class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = localMax = float('-inf')
        for num in nums:
            localMax = max(localMax + num, num)
            globalMax = max(globalMax, localMax)
        return globalMax