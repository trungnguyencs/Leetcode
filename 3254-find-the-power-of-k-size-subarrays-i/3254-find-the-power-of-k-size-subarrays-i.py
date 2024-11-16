class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        l = 0
        ans = []
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1] + 1:
                if r - l + 1 >= k:
                    ans.append(nums[r])
                    continue
            else:
                l = r
            if r >= k - 1:
                ans.append(-1)
        return ans