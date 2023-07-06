class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n): Sliding Window
        minWindow = float('inf')
        s = l = 0
        for r, num in enumerate(nums):
            s += num
            while s >= target:
                minWindow = min(minWindow, r - l + 1)
                s -= nums[l]
                l += 1
        return 0 if minWindow == float('inf') else minWindow
        
        # O(nlogn): Prefix Sum + Binary Search