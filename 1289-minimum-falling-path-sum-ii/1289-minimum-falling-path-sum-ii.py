class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return grid[0][0]
        dp = grid[0]
        for r in range(1, n):
            newDp = [float('inf')]*n
            for c in range(n):
                # by finding Min & secondMin instead of a third level loop time is reduced from O(n^3) to O(n^2)
                Min, minIdx, secondMin, secondMinIdx = self.findMinAndSecondMin(dp)
                newDp[c] = min(newDp[c], grid[r][c] + (Min if c != minIdx else secondMin))
            dp = newDp
        # time: O(n^2), space O(n). We can even further reduce space to O(1) by using just Min, minIdx, secondMin instead of dp array
        return min(dp)
    
    def findMinAndSecondMin(self, arr):
        Min, minIdx, secondMin, secondMinIdx = float('inf'), -1, float('inf'), -1
        for i, num in enumerate(arr):
            if num <= Min:
                Min, minIdx, secondMin, secondMinIdx = num, i, Min, minIdx
            elif num < secondMin:
                secondMin, secondMinIdx = num, i
        return Min, minIdx, secondMin, secondMinIdx