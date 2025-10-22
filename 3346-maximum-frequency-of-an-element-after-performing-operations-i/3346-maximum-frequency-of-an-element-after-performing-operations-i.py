class Solution:
    def maxFrequency(self, nums: List[int], k: int, ops: int) -> int:
        counter = Counter(nums)
        nums.sort()
        maxFreq = 0
        for num in range(nums[0], nums[-1] + 1):
            l = bisect_left(nums, num - k)
            r = bisect_right(nums, num + k) - 1
            freq = min(r - l + 1, counter[num] + ops)
            maxFreq = max(maxFreq, freq)
        return maxFreq