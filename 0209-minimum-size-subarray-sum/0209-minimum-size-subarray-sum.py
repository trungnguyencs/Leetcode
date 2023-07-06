class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n): Sliding Window
        # minWindow = float('inf')
        # s = l = 0
        # for r, num in enumerate(nums):
        #     s += num
        #     while s >= target:
        #         minWindow = min(minWindow, r - l + 1)
        #         s -= nums[l]
        #         l += 1
        # return 0 if minWindow == float('inf') else minWindow
        
        # O(nlogn): Prefix Sum + Binary Search
        minWindow = float('inf')
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for l in range(len(nums)):
            bisectTarget = target + (nums[l-1] if l > 0 else 0)
            r = bisect_left(nums, bisectTarget)
            if r != len(nums):
                minWindow = min(minWindow, r - l + 1)
        return 0 if minWindow == float('inf') else minWindow