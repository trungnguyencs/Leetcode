class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = -1
        for num in numSet:
            if num > 0 and -num in numSet:
                ans = max(ans, num)
        return ans