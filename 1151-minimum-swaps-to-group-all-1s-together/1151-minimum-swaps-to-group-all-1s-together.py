class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        w = nums.count(1)
        zeroCount = 0
        minZeroCount = float('inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            if i >= w and nums[i-w] == 0:
                zeroCount -= 1
            if i >= w - 1:
                minZeroCount = min(minZeroCount, zeroCount)
        return minZeroCount