class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = l = zeroCount = 0
        for r, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
                while zeroCount > 1:
                    if nums[l] == 0:
                        zeroCount -= 1
                    l += 1
            ans = max(ans, r - l + 1)
        return ans