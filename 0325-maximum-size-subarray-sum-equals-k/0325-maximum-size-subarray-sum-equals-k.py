class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maxLen = total = 0
        prefixSum = {0:-1}
        for i, num in enumerate(nums):
            total += num
            if total - k in prefixSum: maxLen = max(maxLen, i - prefixSum[total - k])
            if total not in prefixSum: prefixSum[total] = i
        return maxLen