class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]*len(nums)
        s = 0
        for i, num in enumerate(nums):
            s += num
            if i < 2*k: continue
            if i > 2*k:
                s -= nums[i - 2*k - 1]
            ans[i-k] = s//(2*k + 1)
        return ans