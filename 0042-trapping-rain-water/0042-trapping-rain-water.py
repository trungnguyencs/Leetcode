class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L = [0]*len(height)
        water = 0
        for i in range(1, n):
            L[i] = max(L[i-1], height[i-1])
        R = 0
        for i in range(n - 2, -1, -1):
            R = max(R, height[i+1])
            water += max(0, min(R, L[i]) - height[i])
        return water