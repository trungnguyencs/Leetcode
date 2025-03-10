class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #K different integers = #at most K different integers - #at most K-1 different integers
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)

    def atMostKDistinct(self, nums, k):
        counter = Counter()
        l = ans = 0
        for r, ch in enumerate(nums):
            counter[ch] += 1
            while len(counter) > k:
                prevChar = nums[l]
                counter[prevChar] -= 1
                if counter[prevChar] == 0:
                    del counter[prevChar]
                l += 1
            ans += r - l + 1
        return ans