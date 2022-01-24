class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = [0]*len(height)
        maxLeft = height[0]
        for i in range(1, len(height) - 1):
            left[i] = maxLeft
            maxLeft = max(maxLeft, height[i])
        maxRight = height[-1]
        for i in range(len(height) - 2, 0, -1):
            water += max(0, min(maxRight, left[i]) - height[i])
            maxRight = max(maxRight, height[i])
        return water