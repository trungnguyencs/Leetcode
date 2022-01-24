class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        ans = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                ans.append(str(nums[i]+1))
            if nums[i+1] - nums[i] > 2:
                ans.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
        return ans
