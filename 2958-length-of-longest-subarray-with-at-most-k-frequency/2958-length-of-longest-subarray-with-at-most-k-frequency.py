class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        counter = Counter()
        for r, ch in enumerate(nums):
            counter[ch] += 1
            while counter[ch] > k:
                counter[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans