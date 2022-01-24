class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWater = 0
        while l < r:
            hL, hR = heights[l], heights[r]
            maxWater = max(maxWater, min(hL, hR) * (r - l))
            if hL <= hR:
                l += 1
            else:
                r -= 1
        return maxWater
    