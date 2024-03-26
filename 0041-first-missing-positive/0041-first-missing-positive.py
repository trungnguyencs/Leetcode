class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # marks all numbers that are not in range [1, n]:
        for i, num in enumerate(nums):
            if num <= 0 or num > n:
                nums[i] = n + 1
        for num in nums:
            num = abs(num)
            if num == n + 1: continue
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                return i
        # there is no missing integer in the range [1, n]
        # so the answer is n + 1
        return n + 1