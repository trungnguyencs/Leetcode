class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
    
    def atMost(self, nums, k):
        l = count = window = 0
        for r, num in enumerate(nums):
            window += num % 2
            while window > k:
                window -= nums[l] % 2
                l += 1
            count += r - l + 1
        return count