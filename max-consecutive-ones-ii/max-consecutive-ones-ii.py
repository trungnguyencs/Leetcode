class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = count = maxLen = 0
        for r, num in enumerate(nums):
            if num == 0: count += 1
            while count == 2:
                if nums[l] == 0: count -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen