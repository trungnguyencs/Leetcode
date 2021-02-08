class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = cnt = 0
        for i, num in enumerate(nums):
            if num == 1:
                cnt += 1
                longest = max(longest, cnt)
            else:
                cnt = 0
        return longest
    