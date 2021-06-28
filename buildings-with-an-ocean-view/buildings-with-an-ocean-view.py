class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = heights[-1]
        ans = [len(heights) - 1]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > maxHeight:
                ans.append(i)
                maxHeight = heights[i]
        return ans[::-1]