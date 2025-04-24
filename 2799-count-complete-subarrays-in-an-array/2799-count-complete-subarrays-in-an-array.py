class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        counter = Counter()
        l = ans = 0
        for r, num in enumerate(nums):
            counter[num] += 1
            if len(counter) == k:
                while counter[nums[l]] > 1:
                    counter[nums[l]] -= 1
                    l += 1
                ans += l + 1
        return ans