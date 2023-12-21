class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # BFS solution: do BFS for each pt 1 for the whole grid then find the 0 with min(sum(d))
        # 2D version is just the sum of two 1D versions x and y
        # 1D version: best meeting point is:
        # if odd numbers of points => center pt, if even: any points between the 2 center pts
        # => for both cases, best meeting pt is arr[len(arr)//2]
        R, C = len(grid), len(grid[0])
        rows = [r for r in range(R) for c in range(C) if grid[r][c] == 1]
        cols = [c for r in range(R) for c in range(C) if grid[r][c] == 1]
        return self.minDistance1D(rows) + self.minDistance1D(cols)
        
    def minDistance1D(self, arr):
        arr.sort()
        median = arr[len(arr)//2]
        return sum(abs(num - median) for num in arr)