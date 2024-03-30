class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # approach 1:
        # #subarrays with K different integers = #subarrays with at most K different integers - #subarrays with at most K-1 different integers
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)
        
    def atMostKDistinct(self, nums, k):
        l = count = 0
        counter = Counter()
        for r, num in enumerate(nums):
            counter[num] += 1
            while len(counter) > k:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
            count += r - l + 1
        return count