class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = windowSum = 0
        windowThreshold = k * threshold
        for i, num in enumerate(arr):
            windowSum += num
            if i >= k:
                windowSum -= arr[i - k]
            ans += (i >= k - 1 and windowSum >= windowThreshold)
        return ans   