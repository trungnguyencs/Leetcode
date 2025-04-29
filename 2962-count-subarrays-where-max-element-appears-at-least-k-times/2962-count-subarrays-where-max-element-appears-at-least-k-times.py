class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M = max(nums)
        l = countM = ans = 0
        for r, num in enumerate(nums):
            if num == M:
                countM += 1
            while countM == k:
                if nums[l] == M:
                    countM -= 1
                l += 1
            ans += l #any index from 0 to l - 1 would form a valid subarray
        return ans