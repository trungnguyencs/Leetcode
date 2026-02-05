class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            j = (i + num) % len(nums)
            ans.append(nums[j])
        return ans