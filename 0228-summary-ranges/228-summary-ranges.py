class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            cur = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            ans.append(str(cur) if cur == nums[i] else str(cur) + '->' + str(nums[i]))
            i += 1
        return ans