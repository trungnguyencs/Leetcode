class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numSet = set(nums)
        while original in nums:
            original *= 2
        return original