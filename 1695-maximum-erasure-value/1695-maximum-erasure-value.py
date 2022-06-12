class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = windowSum = ans = 0
        uniq = set()
        for r, num in enumerate(nums):
            windowSum += num
            while num in uniq:
                windowSum -= nums[l]
                uniq.remove(nums[l])
                l += 1
            uniq.add(num)
            ans = max(ans, windowSum)
        return ans