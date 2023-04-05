class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefixSum = 0
        ans = float('-inf')
        for i, num in enumerate(nums):
            prefixSum += num
            ans = max(ans, math.ceil(prefixSum/(i + 1))) # min max when all numbers are equal to their average
        return ans