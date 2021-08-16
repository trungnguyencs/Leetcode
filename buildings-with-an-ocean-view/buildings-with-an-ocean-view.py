class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxRight = heights[-1]
        ans = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxRight:
                ans.append(i)
            maxRight = max(maxRight, heights[i])
        return ans[::-1]