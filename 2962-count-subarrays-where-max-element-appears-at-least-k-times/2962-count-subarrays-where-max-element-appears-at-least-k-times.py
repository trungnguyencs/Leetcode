class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # longest sliding window with at most k-1 freq of max
        M = max(nums)
        l = count = ans = 0
        for r, num in enumerate(nums):
            if num == M:
                count += 1
            while count == k:
                if nums[l] == M:
                    count -= 1
                l += 1
            ans += l
        return ans