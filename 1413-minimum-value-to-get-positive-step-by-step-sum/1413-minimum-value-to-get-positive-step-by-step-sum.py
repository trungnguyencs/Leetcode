class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minPrefixSum = float('inf')
        curSum = 0
        for num in nums:
            curSum += num
            minPrefixSum = min(minPrefixSum, curSum)
        return max(1 - minPrefixSum, 1)