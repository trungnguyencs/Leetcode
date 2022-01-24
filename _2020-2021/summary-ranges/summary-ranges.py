class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        l = 0
        nums.append(float('inf'))
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1] + 1: continue
            if r - l == 1:
                ans.append(str(nums[l]))
            else:
                ans.append(str(nums[l]) + '->' + str(nums[r-1]))
            l = r
        return ans
            
                