class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            if num == 0:
                k -= 1
                while k == -1:
                    if nums[l] == 0:
                        k += 1
                    l += 1
            ans = max(ans, r - l + 1)
        return ans