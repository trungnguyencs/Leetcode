class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        #if sum(nums) is odd, no split is valid. If it's even, all splits are valid
        total = sum(nums)
        if total % 2 == 1: return 0
        return len(nums) - 1