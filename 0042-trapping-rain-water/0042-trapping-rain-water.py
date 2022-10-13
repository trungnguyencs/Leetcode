class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        L = [0]*len(height)
        for i in range(1, len(height)):
            L[i] = max(L[i-1], height[i-1])
        R = 0
        for i in range(len(height) - 2, 0, -1):
            R = max(height[i+1], R)
            water += max(min(L[i], R) - height[i], 0)
        return water