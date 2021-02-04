class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # increase any n-1 numbers by 1
        # is equivalent to decrease any number by 1
        n = len(nums)
        return sum(nums) - n*min(nums)
    