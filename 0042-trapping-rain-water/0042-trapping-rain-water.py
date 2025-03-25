class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        maxRight = ans = 0
        for i in range(len(height) - 2, -1, -1):
            maxRight = max(maxRight, height[i+1])
            ans += max(0, min(maxLeft[i], maxRight) - height[i])
        return ans