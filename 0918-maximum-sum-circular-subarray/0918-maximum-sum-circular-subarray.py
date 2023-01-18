class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        localMax = globalMax = localMin = globalMin = total = nums[0]
        for num in nums[1:]:
            localMax = max(num, localMax + num)
            localMin = min(num, localMin + num)
            globalMax = max(globalMax, localMax)
            globalMin = min(globalMin, localMin)
            total += num
        return globalMax if total == globalMin else max(globalMax, total - globalMin)