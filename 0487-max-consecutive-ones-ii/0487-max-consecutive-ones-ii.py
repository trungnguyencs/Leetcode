class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 1
        maxWindow = l = 0
        for r, num in enumerate(nums):
            if num == 0:
                k -= 1
                while k < 0:
                    if nums[l] == 0:
                        k += 1
                    l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow